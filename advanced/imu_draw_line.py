#
# 加速度センサーの値に応じて直線を描画.
# SH200Qは動作未確認.
#

##################################################
# import
##################################################
import lcd
import image
import math
from machine import I2C

##################################################
# constants
##################################################
MPU6886_ADDRESS             = 0x68
MPU6886_WHOAMI              = 0x75
MPU6886_ACCEL_INTEL_CTRL    = 0x69
MPU6886_SMPLRT_DIV          = 0x19
MPU6886_INT_PIN_CFG         = 0x37
MPU6886_INT_ENABLE          = 0x38
MPU6886_ACCEL_XOUT_H        = 0x3B
MPU6886_TEMP_OUT_H          = 0x41
MPU6886_GYRO_XOUT_H         = 0x43
MPU6886_USER_CTRL           = 0x6A
MPU6886_PWR_MGMT_1          = 0x6B
MPU6886_PWR_MGMT_2          = 0x6C
MPU6886_CONFIG              = 0x1A
MPU6886_GYRO_CONFIG         = 0x1B
MPU6886_ACCEL_CONFIG        = 0x1C
MPU6886_ACCEL_CONFIG2       = 0x1D
MPU6886_FIFO_EN             = 0x23

SH200Q_ADDRESS              = 0x6c
SH200Q_WHOAMI               = 0x30
SH200Q_ACC_CONFIG           = 0x0E
SH200Q_GYRO_CONFIG          = 0x0F
SH200Q_GYRO_DLPF            = 0x11
SH200Q_FIFO_CONFIG          = 0x12
SH200Q_ACC_RANGE            = 0x16
SH200Q_GYRO_RANGE           = 0x2B
SH200Q_OUTPUT_ACC           = 0x00
SH200Q_OUTPUT_GYRO          = 0x06
SH200Q_OUTPUT_TEMP          = 0x0C
SH200Q_REG_SET1             = 0xBA
SH200Q_REG_SET2             = 0xCA
SH200Q_ADC_RESET            = 0xC2
SH200Q_SOFT_RESET           = 0x7F
SH200Q_RESET                = 0x75

x_zero = lcd.width() // 2
y_zero = lcd.height() // 2
x_zero_rot = x_zero
y_zero_rot = y_zero

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

##################################################
# function
##################################################
# I2Cデバイスにデータを送信
def write_i2c(address, value):
    i2c.writeto_mem(MPU6886_ADDRESS, address, bytearray([value]))
    time.sleep_ms(10)

# MPU6886を初期化
def MPU6886_init():
    write_i2c(MPU6886_PWR_MGMT_1, 0x00)
    write_i2c(MPU6886_PWR_MGMT_1, 0x01 << 7)
    write_i2c(MPU6886_PWR_MGMT_1, 0x01 << 0)
    write_i2c(MPU6886_ACCEL_CONFIG, 0x10)
    write_i2c(MPU6886_GYRO_CONFIG, 0x18)
    write_i2c(MPU6886_CONFIG, 0x01)
    write_i2c(MPU6886_SMPLRT_DIV, 0x05)
    write_i2c(MPU6886_INT_ENABLE, 0x00)
    write_i2c(MPU6886_ACCEL_CONFIG2, 0x00)
    write_i2c(MPU6886_USER_CTRL, 0x00)
    write_i2c(MPU6886_FIFO_EN, 0x00)
    write_i2c(MPU6886_INT_PIN_CFG, 0x22)
    write_i2c(MPU6886_INT_ENABLE, 0x01)

# MPU6886からデータを取得
def MPU6886_read(address):
    value = i2c.readfrom_mem(MPU6886_ADDRESS, address, 6)
    value_x = (value[0] << 8 | value[1])
    value_y = (value[2] << 8 | value[3])
    value_z = (value[4] << 8 | value[5])
    if 32768 < value_x:
        value_x = value_x - 65536
    if 32768 < value_y:
        value_y = value_y - 65536
    if 32768 < value_z:
        value_z = value_z - 65536
    return value_x, value_y, value_z

# SH200Qを初期化
def SH200Q_init():
    # FIFO reset
    write_i2c(SH200Q_FIFO_CONFIG, 0x00)
    # Chip ID default = 0x18
    tempdata = i2c.readfrom_mem(SH200Q_ADDRESS, 0x30, 1);
    print ("ChipID:", tempdata);
    # ADCReset
    tempdata = i2c.readfrom_mem(SH200Q_ADDRESS, SH200Q_ADC_RESET, 1);
    tempdata = tempdata[0] | 0x04
    write_i2c(SH200Q_ADC_RESET, tempdata)
    tempdata = tempdata & 0xFB
    write_i2c(SH200Q_ADC_RESET, tempdata)
    tempdata = i2c.readfrom_mem(SH200Q_ADDRESS, 0xD8, 1)
    tempdata = tempdata[0] | 0x80
    write_i2c(0xD8, tempdata)
    tempdata = tempdata & 0x7F;
    write_i2c(0xD8, tempdata)
    write_i2c(0x78, 0x61)
    write_i2c(0x78, 0x00)
    #set acc odr 256hz
    write_i2c(SH200Q_ACC_CONFIG, 0x91)
    # set gyro odr 500hz
    write_i2c(SH200Q_GYRO_CONFIG, 0x13)
    # set gyro dlpf 50hz
    write_i2c(SH200Q_GYRO_DLPF, 0x03)
    # set no buffer mode
    write_i2c(SH200Q_FIFO_CONFIG, 0x00)
    # set acc range +-8G
    write_i2c(SH200Q_ACC_RANGE, 0x01)
    # set gyro range +-2000DPS/s
    write_i2c(SH200Q_GYRO_RANGE, 0x00)
    tempdata = 0xC0;
    write_i2c(SH200Q_REG_SET1, 0xC0)
    tempdata = i2c.readfrom_mem(SH200Q_ADDRESS, SH200Q_REG_SET2, 1)
    tempdata = tempdata[0] | 0x10
    # ADC Reset
    write_i2c(SH200Q_REG_SET2, tempdata)
    tempdata = tempdata | 0xEF
    write_i2c(SH200Q_REG_SET2, tempdata)

# SH200Qからデータを取得
def SH200Q_read(address):
    value = i2c.readfrom_mem(SH200Q_ADDRESS, address, 6)
    value_x = (value[1] << 8 | value[0])
    value_y = (value[3] << 8 | value[2])
    value_z = (value[5] << 8 | value[4])
    if 32768 < value_x:
        value_x = value_x - 65536
    if 32768 < value_y:
        value_y = value_y - 65536
    if 32768 < value_z:
        value_z = value_z - 65536
    return value_x, value_y, value_z

# 1点の座標を回転
def rot1(x_in, y_in, theta):
    x_rot = (x_in - x_zero) * math.cos(theta) -  (y_in - y_zero) * math.sin(theta) + x_zero_rot;
    y_rot = (x_in - x_zero) * math.sin(theta) +  (y_in - y_zero) * math.cos(theta) + y_zero_rot;
    return int(x_rot), int(y_rot)

# 2点の座標を回転
def rot2(x_in1, y_in1, x_in2, y_in2, theta):
    rot_res1 = rot1(x_in1, y_in1, theta)
    rot_res2 = rot1(x_in2, y_in2, theta)
    return rot_res1[0], rot_res1[1], rot_res2[0], rot_res2[1]

def get_drawed_image(theta_x, theta_y, theta_z):
    # 画像を作成
    img = image.Image()
    # y軸の回転に対して直線を描画
    res_y = rot2(0, img.height() // 2, img.width(),img.height() // 2, theta_y)
    img.draw_line(res_y[0], res_y[1], res_y[2], res_y[3], color = (0, 255, 0), thickness = 2)
    return img

##################################################
# main
##################################################
# I2Cデバイスをスキャン
i2c = I2C(I2C.I2C0, freq = 100000, scl = 28, sda = 29)
devices = i2c.scan()
time.sleep_ms(10)
print("i2c", devices)

# I2Cデバイスによって分岐
if devices == [52, MPU6886_ADDRESS]:
    # MPU6886を初期化
    MPU6886_init()
elif devices == [52, SH200Q_ADDRESS]:
    # SH200Qを初期化
    SH200I_init()

# 回転の角度を初期化
rot_theta_x = 0
rot_theta_y = 0
rot_theta_z = 0

while True:
    # I2Cデバイスによって分岐
    if devices == [52, MPU6886_ADDRESS]:
        # MPU6886からデータを取得
        accel_x, accel_y, accel_z = MPU6886_read(MPU6886_ACCEL_XOUT_H)
    elif devices == [52, SH200Q_ADDRESS]:
        # SH200Qからデータを取得
        accel_x, accel_y, accel_z = SH200Q_read(SH200I_OUTPUT_ACC)
    # 回転の角度を計算
    rot_theta_x = 0.5 * rot_theta_y - 0.5 * math.atan2(accel_x, -accel_z)
    rot_theta_y = 0.5 * rot_theta_y - 0.5 * math.atan2(accel_y, -accel_x)
    rot_theta_z = 0.5 * rot_theta_y - 0.5 * math.atan2(accel_z, -accel_y)
    # 画像を描画して取得
    img = get_drawed_image(rot_theta_x, rot_theta_y, rot_theta_z)
    # 画像をLCDに描画
    lcd.display(img)

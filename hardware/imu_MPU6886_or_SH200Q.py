#
# ジャイロ加速度センサー(MPU6886またはSH200Q).
# 動作未確認.
#

##################################################
# import
##################################################
import lcd
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

# 加速度のスケールを計算
aRes = 8.0 / 32768.0;

# 角速度のスケールを計算
gRes = 2000.0 / 32768.0;

while True:
    # I2Cデバイスによって分岐
    if devices == [52, MPU6886_ADDRESS]:
        # MPU6886からデータを取得
        accel_x, accel_y, accel_z = MPU6886_read(MPU6886_ACCEL_XOUT_H)
        gyro_x, gyro_y, gyro_z = MPU6886_read(MPU6886_GYRO_XOUT_H)
        lcd.draw_string(10, 10, "MPU6886")
    elif devices == [52, SH200Q_ADDRESS]:
        # SH200Qからデータを取得
        accel_x, accel_y, accel_z = SH200Q_read(SH200I_OUTPUT_ACC)
        gyro_x, gyro_y, gyro_z = SH200Q_read(SH200Q_OUTPUT_GYRO)
        lcd.draw_string(10, 10, "SH200Q")
    # スケールを反映した値を計算
    accel_array = [accel_x * aRes, accel_y * aRes, accel_z * aRes]
    gyro_array = [gyro_x * gRes, gyro_y * gRes, gyro_z * gRes]
    # 値をコンソールに出力
    print("accel_array: ", accel_array)
    print("gyro_array: ", gyro_array)
    # 値をLCDに描画
    lcd.draw_string(20, 35, "accel_x: %+.10f" % accel_array[0])
    lcd.draw_string(20, 50, "accel_y: %+.10f" % accel_array[1])
    lcd.draw_string(20, 65, "accel_z: %+.10f" % accel_array[2])
    lcd.draw_string(20, 80, "gyro_x: %+.10f" % gyro_array[0])
    lcd.draw_string(20, 95, "gyro_y: %+.10f" % gyro_array[1])
    lcd.draw_string(20, 110, "gyro_z: %+.10f" % gyro_array[2])

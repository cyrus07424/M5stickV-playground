import machine, time, lcd
from machine import I2C

i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, scl=28, sda=29, freq=400000)
#i2c.init(0)
devices = i2c.scan()

print("IC2:", devices)
time.sleep_ms(300)

#SH200Q RESET
#tempdata = i2c.readfrom_mem(108,0x75,1)
#tempdata[0] = tempdata[0] | 0x80
#i2c.writeto_mem(108, 0x75, bytearray(tempdata))
#time.sleep_ms(100)
#tempdata[0] = tempdata[0] & 0x7F
#i2c.writeto_mem(108, 0x75, bytearray(tempdata))

tempdata = i2c.readfrom(108,2)

#ADC Reset
#tempdata = i2c.readfrom_mem(108, 0xC2, 1)
#tempdata = tempdata[0] | 0x04
#i2c.writeto_mem(108, 0xC2, bytearray([tempdata]));
#time.sleep_ms(100)
#tempdata = tempdata[0] | 0xFB
#i2c.writeto_mem(108, 0xC2, bytearray([tempdata]));

tempdata = i2c.readfrom_mem(108, 0x30,1)
print ("ChipID:", tempdata)
time.sleep_ms(100)

tempdata = i2c.readfrom_mem(108, 0xD8, 1)
tempdata = tempdata[0] | 0x80
i2c.writeto_mem(108, 0xD8, bytearray([tempdata]));
time.sleep_ms(100)
tempdata = tempdata & 0x7F;
i2c.writeto_mem(108, 0xD8, bytearray([tempdata]));

i2c.writeto_mem(108, 0x78, bytearray([0x61]));

time.sleep_ms(100)

i2c.writeto_mem(108, 0x78, bytearray([0x00]));

# Accelerometer configuration
i2c.writeto_mem(108, 0x0E, bytearray([0x91]));

# Gyroscope configuration
i2c.writeto_mem(108, 0x0F, bytearray([0x03]));

# Gyroscope configuration1
i2c.writeto_mem(108, 0x11, bytearray([0x13]));

# FIFO configuration
i2c.writeto_mem(108, 0x12, bytearray([0xA0]));

# Accelerometer data format
i2c.writeto_mem(108, 0x16, bytearray([0x01]));

# gyro range
i2c.writeto_mem(108, 0x2B, bytearray([0x00]));


#REG_SET2 ADC RESET
tempdata = i2c.readfrom_mem(108, 0xCA, 1)
tempdata = tempdata[0] | 0x10
i2c.writeto_mem(108, 0xCA, bytearray(tempdata))
time.sleep_ms(100)
tempdata = tempdata & 0xEF
i2c.writeto_mem(108, 0xCA, bytearray(tempdata))
time.sleep_ms(100)

#REG_SET1 RESET
i2c.writeto_mem(108, 0xBA, b'0xC0')
time.sleep_ms(100)
tempdata = i2c.readfrom_mem(108, 0xBA, 1)
tempdata = tempdata[0] & 0xFE
i2c.writeto_mem(108, 0xBA, bytearray([tempdata]));

#DRIVE RESET
tempdata = i2c.readfrom_mem(108, 0xC2, 1)
tempdata = tempdata[0] | 0x10
i2c.writeto_mem(108, 0xC2, bytearray([tempdata]));
time.sleep_ms(100)
tempdata = tempdata & 0xEF
i2c.writeto_mem(108, 0xC2, bytearray([tempdata]));

time.sleep_ms(100)

while True:
    lcd.clear()

    data = i2c.readfrom_mem(108, 0x00, 12)#12バイト分のセンサ・データ読み込み

    accel_x = data[1]#加速度[X]上位バイト取得
    accel_y = data[3]
    accel_z = data[5]
    gyro_x = data[6]#ジャイロ[X]下位バイト取得
    gyro_y = data[8]
    gyro_z = data[10]

    #print ("accel:", accel_x, accel_y, accel_z)
    print ("gyro:", gyro_x, gyro_y, gyro_z)

    lcd.draw_string(10, 10, "accel:" + str(accel_x) + "," + str(accel_y) + "," + str(accel_z), lcd.RED, lcd.BLACK)
    lcd.draw_string(10, 30, "gyro:" + str(gyro_x) + "," + str(gyro_y) + "," + str(gyro_z), lcd.RED, lcd.BLACK)
    time.sleep_ms(200)

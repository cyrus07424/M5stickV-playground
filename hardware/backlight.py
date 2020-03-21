#
# バックライト.
#

##################################################
# import
##################################################
import lcd
import time
from machine import I2C

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init(color = lcd.WHITE)
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

# I2Cデバイスを設定
i2c = I2C(I2C.I2C0, freq = 100000, scl = 28, sda = 29)
devices = i2c.scan()
time.sleep_ms(10)
print("i2c", devices)

##################################################
# function
##################################################
# バックライトの輝度を設定
# 0～8の9段階で指定
def set_backlight(level):
    level = min(level, 8)
    level = max(level, 0)
    val = (level + 7) << 4
    i2c.writeto_mem(0x34, 0x91, int(val))

##################################################
# main
##################################################
level = 0
while True:
    # バックライトの輝度を変更
    level = (level + 1) % 9
    set_backlight(level)
    # LCDに輝度を描画
    lcd.draw_string(lcd.width() // 2, lcd.height() // 2, "level: %d" % level)
    # 1秒待機
    time.sleep(1)

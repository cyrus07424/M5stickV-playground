#
# カメラ画像を動画ファイルとして保存.
# https://www.arduino.cn/thread-92432-1-1.html
#

##################################################
# import
##################################################
import lcd
import sensor
import image
import time
import uos
import video
import sys
from fpioa_manager import *
from machine import I2C
from Maix import I2S, GPIO

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

# レジスタを設定
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)

# GPIO設定
button_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
button_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

##################################################
# main
##################################################
# 変数
basename = "capture"
ext = ".avi"
no = 1

while True:
    while True:
        img = sensor.snapshot()
        img.draw_string(img.width() // 2 - 100, img.height() // 2 - 4, "STOP", color = (0, 0, 255), scale = 2, mono_space = False)
        lcd.display(img)
        if but_a.value() == 0:
            while but_a.value() != 0:
                break
            break
        if but_b.value() == 0:
            sensor.run(0)
            lcd.clear()
            sys.exit()
    lcd.clear()
    print("Start")
    nm = basename + str(no) + ext
    print(nm)
    v = video.open(nm, record = 1)
    while True:
        img = sensor.snapshot()
        img_len = v.record(img)
        img.draw_string(img.width() // 2 - 100, img.height() // 2 - 4, "REC", color = (255, 0, 0), scale = 2, mono_space = False)
        lcd.display(img)
        if but_a.value() == 0:
            while but_a.value() != 0:
                break
            break
    v.record_finish()
    print("Stop")
    lcd.clear()
    no = no + 1

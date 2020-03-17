#
# LED.
#

##################################################
# import
##################################################
from Maix import GPIO
from fpioa_manager import *
from board import board_info

##################################################
# initialize
##################################################
# レジスタを設定
fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

# GPIO設定
led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

##################################################
# main
##################################################
# LEDを消灯(0 = ON, 1 = OFF)
led_w.value(1)
led_r.value(1)
led_g.value(1)
led_b.value(1)

# 1秒待機
time.sleep(1)

while True:
    # LEDを点灯
    # 白
    led_w.value(0)
    led_r.value(1)
    led_g.value(1)
    led_b.value(1)

    # 1秒待機
    time.sleep(1)

    # 赤
    led_w.value(1)
    led_r.value(0)
    led_g.value(1)
    led_b.value(1)

    # 1秒待機
    time.sleep(1)

    # 緑
    led_w.value(1)
    led_r.value(1)
    led_g.value(0)
    led_b.value(1)

    # 1秒待機
    time.sleep(1)

    # 青
    led_w.value(1)
    led_r.value(1)
    led_g.value(1)
    led_b.value(0)

    # 1秒待機
    time.sleep(1)

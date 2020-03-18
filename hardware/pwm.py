#
# PWM.
#

##################################################
# import
##################################################
import time
from machine import Timer,PWM
from board import board_info
from fpioa_manager import fm

##################################################
# main
##################################################
# タイマー設定
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode = Timer.MODE_PWM)

# PWM出力ピン設定
ch = PWM(tim, freq = 500000, duty = 50, pin = board_info.LED_W)

# ループ
duty = 0
dir = True
while True:
    if dir:
        duty += 10
    else:
        duty -= 10
    if 100 < duty:
        duty = 100
        dir = False
    elif duty < 0:
        duty = 0
        dir = True
    time.sleep(0.05)
    ch.duty(duty)

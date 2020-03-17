#
# ボタン.
#

##################################################
# import
##################################################
import sensor
import time
from Maix import GPIO
from fpioa_manager import *
from board import board_info

##################################################
# initialize
##################################################
# レジスタを設定
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)

# GPIO設定
button_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
button_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

##################################################
# main
##################################################
while True:
    # AボタンとBボタンが同時に押されている場合
    if button_a.value() == 0 and button_b.value() == 0:
        time.sleep_ms(200)
        print("Button A and B Press")
    # Aボタンのみ押されている場合
    elif button_a.value() == 0:
        time.sleep_ms(200)
        print("Button A Press")
    # Bボタンのみ押されている場合
    elif button_b.value() == 0:
        time.sleep_ms(200)
        print("Button B Press")

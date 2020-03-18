#
# ボタン.
#

##################################################
# import
##################################################
import sensor
import time
from Maix import GPIO
from fpioa_manager import fm
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
# ボタン押下中フラグ
button_a_pressed = 0
button_b_pressed = 0

while True:
    # Aボタンが押された場合
    if button_a.value() == 0 and button_a_pressed == 0:
        print("Button A Press")
        button_a_pressed = 1
    # Aボタンが放された場合
    if button_a.value() == 1 and button_a_pressed == 1:
        print("Button A release")
        button_a_pressed = 0
    # Bボタンが押された場合
    if button_b.value() == 0 and button_b_pressed == 0:
        print("Button B Press")
        button_b_pressed = 1
    # Bボタンが放された場合
    if button_b.value() == 1 and button_b_pressed == 1:
        print("Button B release")
        button_b_pressed = 0

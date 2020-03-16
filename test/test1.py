#
# Test.
#

##################################################
# import
##################################################
import lcd, image
from fpioa_manager import fm
from board import board_info
from Maix import GPIO
import utime
from machine import Timer, PWM

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

# LED用のGPIO設定
fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)
led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

##################################################
# main
##################################################
# LCDに対して文字を描画
lcd.draw_string(50, 50, "Hello world", lcd.RED, lcd.WHITE)

# 画像を作成(LCDと同じ解像度)
img = image.Image()

# 矩形を指定して画像の一部をコピー
img2 = img.copy((15, 15, 60, 60))

# 2秒待機
time.sleep(2)

# 画像に対して文字を描画
img.draw_string(10, 50, "Hello M5StickV", scale = 2)

# 画像に対して画像を描画
img.draw_image(img2, 30, 30)

# 画像をLCDに描画
lcd.display(img)

# LEDを消灯
led_w.value(1)
led_r.value(1)
led_g.value(1)
led_b.value(1)
time.sleep(2)

# LEDを点灯
# 白
led_w.value(0)
led_r.value(1)
led_g.value(1)
led_b.value(1)
time.sleep(2)

# 赤
led_w.value(1)
led_r.value(0)
led_g.value(1)
led_b.value(1)
time.sleep(2)

# 緑
led_w.value(1)
led_r.value(1)
led_g.value(0)
led_b.value(1)
time.sleep(2)

# 青
led_w.value(1)
led_r.value(1)
led_g.value(1)
led_b.value(0)
time.sleep(2)

# LEDを消灯
led_w.value(1)
led_r.value(1)
led_g.value(1)
led_b.value(1)
time.sleep(2)

# PWM
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode = Timer.MODE_PWM)
ch = PWM(tim, freq = 500000, duty = 50, pin = board_info.LED_W)
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

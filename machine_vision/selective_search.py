#
# Selective Search.
#

##################################################
# import
##################################################
import lcd
import sensor
import image
from random import randint

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

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # Selective Search
    res = img.selective_search(threshold = 200, size = 20, a1 = 0.5, a2 = 1.0, a3 = 1.0)
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 矩形を描画
        img.draw_rectangle(i, color = (randint(100, 255), randint(100, 255), randint(100, 255)))
    # 画像をLCDに描画
    lcd.display(img)

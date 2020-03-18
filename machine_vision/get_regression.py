#
# 線形回帰を取得.
# https://docs.openmv.io/library/omv.image.html#image.image.get_regression
# https://github.com/openmv/openmv/blob/master/scripts/examples/09-Feature-Detection/linear_regression_fast.py
#

##################################################
# import
##################################################
import lcd
import sensor
import image

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.run(1)

##################################################
# main
##################################################
# しきい値
THRESHOLD = (0, 100)

# 二値化の結果を可視化するかどうかの設定
BINARY_VISIBLE = True

while True:
    # カメラ画像を取得
    img = sensor.snapshot().binary([THRESHOLD]) if BINARY_VISIBLE else sensor.snapshot()
    # 線形回帰を取得
    line = img.get_regression([(255, 255) if BINARY_VISIBLE else THRESHOLD])
    # 結果が存在する場合
    if line:
        # 直線を描画
        img.draw_line(line.line(), color = 127)
    # 画像をLCDに描画
    lcd.display(img)

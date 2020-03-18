#
# 二値化.
# https://docs.openmv.io/library/omv.image.html#image.image.binary
#

##################################################
# import
##################################################
import lcd
import sensor

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
# しきい値
thresholds = (90, 100, -128, 127, -128, 127)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 二値化
    img.binary([thresholds], invert = False, zero = True)
    # 画像をLCDに描画
    lcd.display(img)

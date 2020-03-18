#
# 直交座標から極座標へ変換.
# https://docs.openmv.io/library/omv.image.html#image.image.linpolar
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
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 直交座標から極座標へ変換(reverse = Trueで逆変換)
    img.linpolar(reverse = False)
    # 画像をLCDに描画
    lcd.display(img)

#
# レンズ補正.
# https://docs.openmv.io/library/omv.image.html#image.image.lens_corr
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
    # レンズ補正
    img.lens_corr(strength = 1.8, zoom = 0.8)
    # 画像をLCDに描画
    lcd.display(img)

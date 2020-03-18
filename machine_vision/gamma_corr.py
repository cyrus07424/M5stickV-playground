#
# ガンマ補正.
# https://docs.openmv.io/library/omv.image.html#image.image.gamma_corr
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
    # ガンマ補正
    img.gamma_corr(gamma = 0.5, contrast = 1.0, brightness = 0.0)
    # 画像をLCDに描画
    lcd.display(img)

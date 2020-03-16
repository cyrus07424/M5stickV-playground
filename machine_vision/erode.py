#
# 近似色領域を囲む線を消去.
#

##################################################
# import
##################################################
import sensor
import lcd

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(True)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 近似色領域を囲む線を消去
    img.erode(1)
    # 画像をLCDに描画
    lcd.display(img)

#
# ヒストグラム平坦化.
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
    # ヒストグラム平坦化
    img.histeq()
    # 画像をLCDに描画
    lcd.display(img)

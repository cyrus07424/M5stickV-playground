#
# 物体を検出.
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

# ゲインを設定
sensor.set_gainceiling(8)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 輪郭を検出
    img.find_edges(image.EDGE_SIMPLE, threshold = (100, 255))
    # クロージング処理
    img.close(3)    

    # TODO

    # 画像をLCDに描画
    lcd.display(img)

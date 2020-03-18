#
# 輪郭を検出.
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
# 画像フォーマットはグレースケールのみ対応
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.run(1)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # ガウシアンフィルタを適用
    img.gaussian(3)
    # 輪郭を検出
    img.find_edges(image.EDGE_CANNY, threshold = (50, 100))
    # 近似色領域を囲む線を描画
    img.dilate(2)
    # 画像をLCDに描画
    lcd.display(img)

#
# エッジ検出フィルタ.
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
# フィルタ定義
edge = (-1, -1, -1, -1, 8, -1, -1, -1, -1)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # フィルタを適用
    img.conv3(edge)
    # 画像をLCDに描画
    lcd.display(img)

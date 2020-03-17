#
# 緑色の物体を検出.
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
# green_threshold
green_threshold  = (0, 80, -70, -10, -0, 30)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # blobを検出
    blobs = img.find_blobs([green_threshold])
    # 結果が存在する場合
    if blobs:
        # 全ての結果に対して実行
        for b in blobs:
            # 矩形を描画
            tmp = img.draw_rectangle(b[0:4])
            # 十字を描画
            tmp = img.draw_cross(b[5], b[6])
    # 画像をLCDに描画
    lcd.display(img)

#
# AprilTagを検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_apriltags
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
# QVGAは最大サポート解像度を超えるためQQVGAを設定
sensor.set_framesize(sensor.QQVGA)
sensor.run(1)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # AprilTagを検出
    res = img.find_apriltags()
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 矩形を描画
        img.draw_rectangle(i.x(), i.y(), i.w(), i.h(), color = (255, 0, 0), thickness = 2)
        # 十字を描画
        img.draw_cross(i.cx(), i.cy(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

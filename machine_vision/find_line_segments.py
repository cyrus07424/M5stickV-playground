#
# 線分を検出.
# (検出件数が多いとフリーズする).
# https://docs.openmv.io/library/omv.image.html#image.image.find_line_segments
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
sensor.set_framesize(sensor.QQVGA)
sensor.run(1)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 線分を検出
    res = img.find_line_segments()
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 直線を描画
        img.draw_line(i.x1(), i.y1(), i.x2(), i.y2(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

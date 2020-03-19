#
# 円を検出.
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
    # 円を検出
    res = img.find_circles(threshold = 3500, x_margin = 10, y_margin = 10, r_margin = 10, r_min = 2, r_max = 100, r_step = 2)
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 円を描画
        img.draw_circle(i.x(), i.y(), i.r(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

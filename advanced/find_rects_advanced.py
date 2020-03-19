#
# 矩形を検出.
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
    # 矩形を検出
    res = img.find_rects()
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 矩形を描画
        img.draw_rectangle(i.x(), i.y(), i.w(), i.h(), color = (255, 0, 0), thickness = 2)
        # 四隅の座標に対して実行
        for p in i.corners():
            # 円を描画
            img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
        # 四隅を繋ぐ辺に対して実行
        for j in range(4):
            p1 = i.corners()[j]
            p2 = i.corners()[(j + 1) % 4]
            # 直線を描画
            img.draw_line(p1[0], p1[1], p2[0], p2[1], color = (0, 0, 255))
    # 画像をLCDに描画
    lcd.display(img)

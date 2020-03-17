#
# 円を検出.
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
while(True):
    # カメラ画像を取得
    img = sensor.snapshot()
    # 円を検出
    res = img.find_circles()
    # 結果が存在する場合
    if res:
        # 全ての結果に対して実行
        for i in res:
            print(i)
            if 20 < i.r():
                # 円を描画
                img.draw_circle(i.x(), i.y(), i.r(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

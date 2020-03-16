#
# 直線を検出.
# 検出された直線の座標は画像のある1辺から向かいの辺までとなる.
#

##################################################
# import
##################################################
import sensor
import image
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
while(True):
    # カメラ画像を取得
    img = sensor.snapshot()
    # 直線を検出
    res = img.find_lines()
    # 結果が存在する場合
    if res:
        # 全ての結果に対して実行
        for i in res:
            print(i)
            # 直線を描画
            img.draw_line(i.x1(), i.y1(), i.x2(), i.y2(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

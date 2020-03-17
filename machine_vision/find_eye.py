#
# 瞳を検出.
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
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
# 画像フォーマットはグレースケールのみ対応
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.run(True)

##################################################
# main
##################################################
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 瞳を検出
    res = img.find_eye((0, 0, img.width(), img.height()))
    # 結果が存在する場合
    if res != (0, 0):
        print(res)
        # 十字を描画
        img.draw_cross(res[0], res[1], thickness = 2, size = 20)
    # 画像をLCDに描画
    lcd.display(img)

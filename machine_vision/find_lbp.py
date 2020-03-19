#
# Local Binary Patternを検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_lbp
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
    # Local Binary Patternを検出
    res = img.find_lbp((0, 0, img.width(), img.height()))
    # 結果が存在する場合
    if res:
        print(res)
        # TODO
    # 画像をLCDに描画
    lcd.display(img)

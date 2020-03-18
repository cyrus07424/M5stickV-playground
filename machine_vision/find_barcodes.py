#
# バーコードを検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_barcodes
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
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # バーコードを検出
    res = img.find_barcodes()
    # 結果が存在する場合
    if res:
        # 全ての結果に対して実行
        for i in res:
            print(i)
            # 矩形を描画
            img.draw_rectangle(i.x(), i.y(), i.w(), i.h(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

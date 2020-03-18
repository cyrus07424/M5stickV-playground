#
# QRコードをスキャン.
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
    # QRコードを検出
    res = img.find_qrcodes()
    # 結果が存在する場合
    if res:
        # 先頭の結果に対して実行
        # QRコードの内容を描画
        img.draw_string(img.width() // 2 - 100, img.height() // 2 - 4, res[0].payload(), color = (0, 128, 0), scale = 2, mono_space = False)
        # QRコードの内容をコンソールに出力
        print(res[0].payload())
    # 画像をLCDに描画
    lcd.display(img)

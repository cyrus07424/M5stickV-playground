#
# QRコードをスキャン.
#

##################################################
# import
##################################################
import sensor
import image
import lcd
import time

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

# タイマーを初期化
clock = time.clock()

##################################################
# main
##################################################
while True:
    # タイマーをカウント
    clock.tick()
    # カメラ画像を取得
    img = sensor.snapshot()
    # QRコードを検出
    res = img.find_qrcodes()
    # fpsを取得
    fps = clock.fps()
    # 結果が存在する場合
    if res:
        # 全ての結果に対して実行
        for i in res:
            # QRコードの内容を描画
            img.draw_string(img.width() // 2 - 100, img.height() // 2 - 4, i.payload(), color = (0, 128, 0), scale = 2, mono_space = False)
            # QRコードの内容をコンソールに出力
            print(i.payload())
    # 画像をLCDに描画
    lcd.display(img)

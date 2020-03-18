#
# fpsを描画.
#

##################################################
# import
##################################################
import lcd
import sensor
import image
import time

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
    # fpsを取得
    fps = clock.fps()
    fps_string = "%.2ffps" % fps
    # fpsを描画
    img.draw_string(img.width() // 4, img.height() // 2, fps_string, color = (0, 128, 0), scale = 2)
    # 画像をLCDに描画
    lcd.display(img)
    # fpsをコンソールに出力
    print(fps_string)

#
# fpsを描画.
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
# 最初の30フレームをスキップする(fps値を安定させるため?)
sensor.skip_frames(30)

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
    # fpsを描画
    img.draw_string(100, 100, ("%2.1ffps" %(fps)), color = (0, 128, 0), scale = 2)
    # 画像をLCDに描画
    lcd.display(img)

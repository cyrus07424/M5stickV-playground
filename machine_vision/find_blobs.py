#
# しきい値から物体を検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_blobs
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
# しきい値
thresholds_red = (30, 100, 15, 127, 15, 127)
thresholds_green = (30, 100, -64, -8, -32, 32)
thresholds_green2  = (0, 80, -70, -10, -0, 30)
thresholds_blue = (0, 30, 0, 64, -128, 0)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # blobを検出
    res = img.find_blobs([thresholds_red], area_threshold = 50)
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 矩形を描画
        img.draw_rectangle(i.x(), i.y(), i.w(), i.h(), color = (255, 0, 0), thickness = 2)
        # 十字を描画
        img.draw_cross(i.cx(), i.cy(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

#
# キーポイント.
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
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_auto_gain(False, value = 100)
sensor.run(1)

##################################################
# function
##################################################
def draw_keypoints(img, kpts):
    if kpts:
        print(kpts)
        img.draw_keypoints(kpts)
        img = sensor.snapshot()
        time.sleep(1)

##################################################
# main
##################################################
# キーポイント
kpts1 = None

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    if kpts1 == None:
        kpts1 = img.find_keypoints(max_keypoints = 150, threshold = 10, scale_factor = 1.2)
        draw_keypoints(img, kpts1)
    else:
        kpts2 = img.find_keypoints(max_keypoints = 150, threshold = 10, normalized = True)
        if (kpts2):
            match = image.match_descriptor(kpts1, kpts2, threshold=85)
            if 10 < match.count():
                img.draw_rectangle(match.rect())
                img.draw_cross(match.cx(), match.cy(), size = 10)
            print(kpts2, "matched: %d dt:%d" % (match.count(), match.theta()))
            img.draw_keypoints(kpts2, size = 5, matched = True)
    # 画像をLCDに描画
    lcd.display(img)

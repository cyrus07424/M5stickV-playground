#
# 特徴を検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_features
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
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

# コントラスト設定
sensor.set_contrast(3)
# ゲイン設定
sensor.set_gainceiling(16)

##################################################
# main
##################################################
# カスケード情報を取得(目)
cascade = image.HaarCascade("eye", stages = 24)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 特徴を検出
    res = img.find_features(cascade, threshold = 0.5, scale = 1.5)
    # 全ての結果に対して実行
    for i in res:
        print(i)
        # 矩形を描画
        img.draw_rectangle(i, thickness = 2)
        # 瞳を検出
        iris = img.find_eye(i)
        # 十字を描画
        img.draw_cross(iris[0], iris[1])
    # 画像をLCDに描画
    lcd.display(img)

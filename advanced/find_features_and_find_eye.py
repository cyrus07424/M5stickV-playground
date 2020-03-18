#
# 特徴を検出、瞳を検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_features
# https://docs.openmv.io/library/omv.image.html#image.image.find_eye
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
# カスケード情報を取得(顔)
cascade_frontalface = image.HaarCascade("frontalface")
# カスケード情報を取得(目)
cascade_eye = image.HaarCascade("eye")

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 特徴を検出(顔)
    res_frontalface = img.find_features(cascade_frontalface)
    # 結果が存在する場合
    if res_frontalface:
        # 全ての結果に対して実行
        for i in res_frontalface:
            print(i)
            # 矩形を描画(顔)
            img.draw_rectangle(i)
            # 特徴を検出(目)
            res_eye = img.find_features(cascade_eye, roi = i)
            # 結果が存在する場合
            if res_eye:
                # 全ての結果に対して実行
                for j in res_eye:
                    print(j)
                    # 矩形を描画(目)
                    img.draw_rectangle(j)
                    # 瞳を検出
                    iris = img.find_eye(j)
                    # 十字を描画
                    img.draw_cross(iris[0], iris[1])
    # 画像をLCDに描画
    lcd.display(img)

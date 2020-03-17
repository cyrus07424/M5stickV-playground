#
# 画像の変化量を積算.
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
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
# センサーサイズのsensor.B64X64は使用不可のため、set_windowingメソッドを利用して取得画像のサイズを64x64に設定する
sensor.set_framesize(sensor.QQVGA)
sensor.set_windowing((64, 64))
sensor.run(True)

##################################################
# main
##################################################
x = 0.0
y = 0.0
oldImage = sensor.snapshot()
while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 画像をLCDに描画
    lcd.display(img)
    # displacementオブジェクトを取得
    result = img.find_displacement(oldImage)
    # 縦横方向の移動量（画像変化量）を取得
    x += result.x_translation()
    y += result.y_translation()
    # 四捨五入
    x = round(x, 3)
    y = round(y, 3)
    # 変数をコピー
    oldImage = img.copy()
    # 結果をコンソールに出力
    print("x: ", x, "y: ", y)
    print(result)

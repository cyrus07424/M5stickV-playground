#
# テンプレートを検出.
# https://docs.openmv.io/library/omv.image.html#image.image.find_template
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
sensor.set_framesize(sensor.QQVGA)
sensor.run(1)

##################################################
# main
##################################################
# FIXME テンプレート用画像を作成
template = image.Image()
template_gray = template.to_grayscale()
template_gray = template_gray.copy([0, 0, 50, 50])
template_gray.draw_string(0, 0, "Hello", color = (255, 255, 255))
template_gray.negate()

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # テンプレートを検出
    res = img.find_template(template_gray, 0.5)
    # 結果が存在する場合
    if res:
        print(res)
        # 矩形を描画
        img.draw_rectangle(res[0], res[1], res[2], res[3], color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

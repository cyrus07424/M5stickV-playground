#
# 画像を保存・読み込み.
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
# 画像ファイルの保存先パス
path = "image_save_read.jpg"

# カメラ画像を取得
img = sensor.snapshot()

# 画像を保存
print("save image")
img.save(path, quality = 95)

# 画像を読み込み
print("read image")
img_read = image.Image(path)

# 画像をLCDに描画
lcd.display(img_read)
print("ok")

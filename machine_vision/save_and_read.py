#
# 画像を保存・読み込み.
#

##################################################
# import
##################################################
import sensor, lcd, image

##################################################
# initialize
##################################################
print("init")

# LCDを初期化
lcd.init()
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

# カメラを初期化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(True)

print("init ok")

##################################################
# main
##################################################
# 画像ファイルの保存先パス
path = "image_save_read.jpg"

# カメラ画像を取得
img = sensor.snapshot()

# 画像を保存
print("save image")
img.save(path)

# 画像を読み込み
print("read image")
img_read = image.Image(path)

# 画像をLCDに描画
lcd.display(img_read)
print("ok")

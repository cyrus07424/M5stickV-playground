#
# LCD.
#

##################################################
# import
##################################################
import lcd, time
import image

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を標準デモアプリの方向へ合わせる
lcd.direction(lcd.YX_LRUD)

##################################################
# main
##################################################
# LDCをクリア(色を指定)
lcd.clear(lcd.BLUE)

# 2秒待機
time.sleep(2)

# LCDに対して文字を描画
lcd.draw_string(100, 100, "hello maixpy", lcd.WHITE, lcd.BLACK)

# 2秒待機
time.sleep(2)

# 画像を作成(LCDと同じ解像度)
img = image.Image()

# 画像に対して文字を描画
img.draw_string(10, 10, "hello maixpy", scale = 2)

# 画像に対して矩形を描画
img.draw_rectangle((50, 50, 30, 30))

# 画像をLCDに描画
lcd.display(img)

#
# 円を描画.
# https://maixpy.sipeed.com/en/libs/machine_vision/image.html#imagedrawcirclex-y-radius-color-thickness1-fillfalse
#

##################################################
# import
##################################################
import lcd
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
# 画像を作成
img = image.Image()

# 画像に対して円を描画(x, y, radius)
img.draw_circle(img.width() // 2, img.height() // 2, img.height() // 2 - 2)

# 画像をLCDに描画
lcd.display(img)

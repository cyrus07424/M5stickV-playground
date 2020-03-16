#
# 十字を描画.
# https://maixpy.sipeed.com/en/libs/machine_vision/image.html#imagedrawcrossx-y-color-size5-thickness1
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

# 画像に対して十字を描画(x, y)
img.draw_cross(img.width() // 2, img.height() // 2, size = 10)

# 画像をLCDに描画
lcd.display(img)

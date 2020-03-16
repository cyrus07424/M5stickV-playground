#
# 矢印を描画.
# https://maixpy.sipeed.com/en/libs/machine_vision/image.html#imagedrawarrowx0-y0-x1-y1-color-thickness1
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

# 画像に対して矢印を描画(x0, y0, x1, y1)
img.draw_arrow(img.width() // 4, img.height() // 4, img.width() // 4 * 3, img.height() // 4 * 3)

# 画像をLCDに描画
lcd.display(img)

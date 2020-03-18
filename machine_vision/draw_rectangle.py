#
# 矩形を描画.
# https://maixpy.sipeed.com/en/libs/machine_vision/image.html#imagedrawrectanglex-y-w-h-color-thickness1-fillfalse
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
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

##################################################
# main
##################################################
# 画像を作成
img = image.Image()

# 画像に対して矩形を描画(x, y, w, h)
img.draw_rectangle(5, 5, img.width() - 5, img.height() - 5, thickness = 2)

# 画像をLCDに描画
lcd.display(img)

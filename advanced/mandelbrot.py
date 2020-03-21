#
# マンデルブロ集合を描画.
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
# function
##################################################
def in_set(c):
    z = 0
    for i in range(40):
        z = z * z + c
        if abs(z) > 60:
            return False
    return True

##################################################
# main
##################################################
# 画像を作成
img = image.Image()

# マンデルブロ集合を描画
for u in range(img.width()):
    for v in range(img.height()):
        if in_set((u / (img.width() // 3) - 2) + (v / (img.height() // 2) - 1) * 1j):
            img.set_pixel(u, v, color = (255, 0, 0))

# 画像をLCDに描画
lcd.display(img)

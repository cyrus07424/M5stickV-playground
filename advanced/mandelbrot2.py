#
# マンデルブロ集合を描画.
#

##################################################
# import
##################################################
import lcd
import image

##################################################
# constants
##################################################
center = (3, 1.5)
iterate_max = 100
colors_max = 100

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
def iterate_mandelbrot(c, z = 0):
    for n in range(iterate_max + 1):
        z = z * z + c
        if abs(z) > 2:
            return n
    return None

# HSV to RGB
# h = 0.0 ~ 1.0
# s = 0.0 ~ 1.0
# v = 0.0 ~ 1.0
def hsv_to_rgb(h, s, v):
    h = h * 360
    s = s * 255
    v = v * 255

    i = int(h / 60.0)
    mx = v
    mn = v - ((s / 255.0) * v)

    if h is None:
        return(0, 0, 0)
    if i == 0:
        (r1, g1, b1) = (mx, (h / 60.0) * (mx - mn) + mn, mn)
    elif i == 1:
        (r1, g1, b1) = (((120.0 - h) / 60.0) * (mx - mn) + mn, mx, mn)
    elif i == 2:
        (r1, g1, b1) = (mn, mx, ((h - 120.0) / 60.0) * (mx - mn) + mn)
    elif i == 3:
        (r1, g1, b1) = (mn, ((240.0 - h) / 60.0) * (mx - mn) + mn, mx)
    elif i == 4:
        (r1, g1, b1) = (((h - 240.0) / 60.0) * (mx - mn) + mn, mn, mx)
    elif 5 <= i:
        (r1, g1, b1) = (mx, mn, ((360.0 - h) / 60.0) * (mx - mn) + mn)
    return (int(r1), int(g1), int(b1))

##################################################
# main
##################################################
# カラーパレットを初期化
palette = [0] * colors_max
for i in range(colors_max):
    f = 1 - abs((float(i) / colors_max - 1) ** 15)
    r, g, b = hsv_to_rgb(.66 + f / 3, 1 - f / 2, f)
    palette[i] = (r, g, b)

# 画像を作成
img = image.Image()

# スケールを計算
scale = 1.0 / (img.height() / 3)

# マンデルブロ集合を描画
for x in range(img.width()):
    for y in range(img.height()):
        c = complex(x * scale - center[0], y * scale - center[1])
        n = iterate_mandelbrot(c)
        if n is None:
            v = 1
        else:
            v = n / 100.0
        img.set_pixel(x, y, color = palette[int(v * (colors_max - 1))])
# 画像をLCDに描画
lcd.display(img)

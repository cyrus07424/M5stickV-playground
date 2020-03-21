#
# 3Dキューブを描画.
# https://forums.openmv.io/viewtopic.php?t=1020
#

##################################################
# import
##################################################
import lcd
import image
import math

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
def mat_mult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if(cols_A != rows_B):
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return None

    C = [[0.0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

def scale(x, y, z):
    m = [
        [ x, 0, 0, 0 ],
        [ 0, y, 0, 0 ],
        [ 0, 0, z, 0 ],
        [ 0, 0, 0, 1 ],
    ]
    return m

def rotate_x(a):
    s = math.sin(a)
    c = math.cos(a)
    m = [
        [ 1, 0, 0, 0 ],
        [ 0, c,-s, 0 ],
        [ 0, s, c, 0 ],
        [ 0, 0, 0, 1 ],
    ]
    return m

def rotate_y(a):
    s = math.sin(a)
    c = math.cos(a)
    m = [
        [ c, 0, s, 0 ],
        [ 0, 1, 0, 0 ],
        [-s, 0, c, 0 ],
        [ 0, 0, 0, 1 ],
    ]
    return m

def rotate_z(a):
    s = math.sin(a)
    c = math.cos(a)
    m = [
        [ c,-s, 0, 0 ],
        [ s, c, 0, 0 ],
        [ 0, 0, 1, 0 ],
        [ 0, 0, 0, 1 ],
    ]
    return m

def rotate(rx, ry, rz):
    m = rotate_z(rz)
    m = mat_mult(rotate_y(ry), m)
    m = mat_mult(rotate_x(rx), m)
    return m

def translate(x, y, z):
    m = [
        [ 1, 0, 0, x ],
        [ 0, 1, 0, y ],
        [ 0, 0, 1, z ],
        [ 0, 0, 0, 1 ],
    ]
    return m

def point(x, y, z):
    m = [ [x], [y], [z], [1] ]
    return m

##################################################
# constants
##################################################
points_pairs = [
    [point(0, 0, 0), point(0, 1, 0)],
    [point(0, 1, 0), point(1, 1, 0)],
    [point(1, 1, 0), point(1, 0, 0)],
    [point(1, 0, 0), point(0, 0, 0)],

    [point(0, 0, 1), point(0, 1, 1)],
    [point(0, 1, 1), point(1, 1, 1)],
    [point(1, 1, 1), point(1, 0, 1)],
    [point(1, 0, 1), point(0, 0, 1)],

    [point(0, 0, 0), point(0, 0, 1)],
    [point(0, 1, 0), point(0, 1, 1)],
    [point(1, 1, 0), point(1, 1, 1)],
    [point(1, 0, 0), point(1, 0, 1)],
]

colors = [
    [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0],
    [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0],
    [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255],
]

##################################################
# main
##################################################
sx, sy, sz = 100, 100, 100
rx, ry, rz = 0, math.pi / 6, math.pi / 6
tx, ty, tz = lcd.width() / 4, lcd.height() / 2, 100

# カウンタ
i = 0

while True:
    # カウンタを加算
    i = i + 1
    # x軸の回転を計算
    rx = i * math.pi / 100
    # 画像を作成
    img = image.Image()
    # 全ての辺に対して実行
    for point_pair, color in zip(points_pairs, colors):
        m = point_pair[0]
        m = mat_mult(scale(sx, sy, sz), m)
        m = mat_mult(rotate(rx, ry, rz), m)
        m = mat_mult(translate(tx, ty, tz), m)
        m0 = m

        m = point_pair[1]
        m = mat_mult(scale(sx, sy, sz), m)
        m = mat_mult(rotate(rx, ry, rz), m)
        m = mat_mult(translate(tx, ty, tz), m)
        m1 = m

        x0, y0, x1, y1 = int(m0[0][0]), int(m0[1][0]), int(m1[0][0]), int(m1[1][0])
        # 直線を描画
        img.draw_line(x0, y0, x1, y1, color = color, thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

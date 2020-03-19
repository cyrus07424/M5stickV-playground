#
# AprilTagを検出して3Dキューブを描画.
# https://docs.openmv.io/library/omv.image.html#image.image.find_apriltags
# https://forums.openmv.io/viewtopic.php?t=1020
#

##################################################
# import
##################################################
import lcd
import sensor
import math

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
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.run(1)

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

# 2点間の距離を取得
def get_distance(p1, p2):
    d = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return d

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
# f_x is the x focal length of the camera. It should be equal to the lens focal length in mm
# divided by the x sensor size in mm times the number of pixels in the image.
# The below values are for the OV7725 camera with a 2.8 mm lens.

# f_y is the y focal length of the camera. It should be equal to the lens focal length in mm
# divided by the y sensor size in mm times the number of pixels in the image.
# The below values are for the OV7725 camera with a 2.8 mm lens.

# c_x is the image x center position in pixels.
# c_y is the image y center position in pixels.
f_x = (2.8 / 3.984) * sensor.width()
f_y = (2.8 / 2.952) * sensor.height()
c_x = sensor.width() // 2
c_y = sensor.height() // 2

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # AprilTagを検出
    res = img.find_apriltags(fx = f_x, fy = f_y, cx = c_x, cy = c_y)
    # 全ての結果に対して実行
    for i in res:
        # 十字を描画
        img.draw_cross(i.cx(), i.cy(), color = (255, 255, 255), thickness = 2)

        # 辺の長さを取得
        edge_length = sum([
            get_distance(i.corners()[0], i.corners()[1]),
            get_distance(i.corners()[1], i.corners()[2]),
            get_distance(i.corners()[2], i.corners()[3]),
            get_distance(i.corners()[3], i.corners()[0])
        ]) / 4

        # 回転行列を計算
        sx, sy, sz = edge_length, edge_length, edge_length
        rx, ry, rz = i.x_rotation(), i.y_rotation(), i.z_rotation()
        tx, ty, tz = i.x_translation() + i.x(), i.y_translation() + i.y() + i.h(), i.z_translation()

        # 全ての辺に対して実行
        for point_pair, color in zip(points_pairs, colors):
            # 3次元空間上の点を計算
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

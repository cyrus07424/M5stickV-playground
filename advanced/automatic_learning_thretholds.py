#
# しきい値を自動で学習.
# https://www.arduino.cn/thread-93471-1-1.html
#

##################################################
# import
##################################################
import lcd
import sensor
import image

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
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

##################################################
# function
##################################################
# 最大のblobを取得
def find_max(blobs):
    max_size = 0
    for blob in blobs:
        if max_size < blob[2] * blob[3]:
            max_blob = blob
            max_size = blob[2] * blob[3]
    return max_blob

##################################################
# main
##################################################
# 学習対象の範囲
rect_width = 50
rect_height = 50
r = [(sensor.width() // 2) - (rect_width // 2), (sensor.height() // 2) - (rect_height // 2), rect_width, rect_height]

# 準備
for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)
    lcd.display(img)
    lcd.draw_string(0, 0, "Learning thresholds in %d ..." % (60 - i))

# しきい値を学習
threshold = [0, 0, 0, 0, 0, 0]
for i in range(60):
    img = sensor.snapshot()
    hist = img.get_histogram(roi = r)
    lo = hist.get_percentile(0.05)
    hi = hist.get_percentile(0.95)
    threshold[0] = (threshold[0] + lo.l_value()) // 2
    threshold[1] = (threshold[1] + hi.l_value()) // 2
    threshold[2] = (threshold[2] + lo.a_value()) // 2
    threshold[3] = (threshold[3] + hi.a_value()) // 2
    threshold[4] = (threshold[4] + lo.b_value()) // 2
    threshold[5] = (threshold[5] + hi.b_value()) // 2
    for blob in img.find_blobs([threshold], pixels_threshold = 50, area_threshold = 50, merge = True, margin = 2):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        img.draw_rectangle(r)
        lcd.display(img)
    lcd.draw_string(0, 0, "Learning now...")

# 学習結果をコンソールに出力
print("threshold: ", threshold)

# 学習結果を適用
while True:
    img = sensor.snapshot()
    blobs = img.find_blobs([threshold], pixels_threshold = 50, area_threshold = 50, merge = True, margin = 2)
    if blobs:
        max_blob = find_max(blobs)
        img.draw_rectangle(max_blob.rect())
        img.draw_cross(max_blob.cx(), max_blob.cy())
    lcd.display(img)
    lcd.draw_string(0, 0, "Tracking colors...")

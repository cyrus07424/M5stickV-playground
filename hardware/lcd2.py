#
# LCD(カラーバー).
#

##################################################
# import
##################################################
import lcd, image, time

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
# サイズを指定して画像を作成
img = image.Image(size = (240, 240))

# 画像に対して矩形を描画
img.draw_rectangle(0, 0, 30, 240, fill = True, color = (0xff, 0xff, 0xff))
img.draw_rectangle(30, 0, 30, 240, fill = True, color = (250, 232, 25))
img.draw_rectangle(60, 0, 30, 240, fill = True, color = (106, 198, 218))
img.draw_rectangle(90, 0, 30, 240, fill = True, color = (98, 177, 31))
img.draw_rectangle(120, 0, 30, 240, fill = True, color = (180, 82, 155))
img.draw_rectangle(150, 0, 30, 240, fill = True, color = (231, 47, 29))
img.draw_rectangle(180, 0, 30, 240, fill = True, color = (32, 77, 158))
img.draw_rectangle(210, 0, 30, 240, fill = True, color = (27, 28, 32))

# 画像をLCDに描画
lcd.display(img)

# 描画の時間を計測
count = 50
while 0 < count:
    # 現在の時刻をミリ秒で取得
    t = time.ticks_ms()
    # 画像をLCDに描画
    lcd.display(img)
    # 画像をLCDに描画する処理にかかった時間(ミリ秒)をコンソールに出力
    print(time.ticks_ms() - t)
    count -= 1

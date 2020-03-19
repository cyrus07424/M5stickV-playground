#
# 顔認識.
#

##################################################
# import
##################################################
import lcd
import sensor
import image
import KPU as kpu

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
# main
##################################################
# モデルを読み込み(ファームウェアの0x300000番地を指定)
task = kpu.load(0x300000)

# Anchor data is for bbox, extracted from the training sets.
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)

# モデルを初期化
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 推論を実行
    res = kpu.run_yolo2(task, img)
    # 結果が存在する場合
    if res:
        # 全ての結果に対して実行
        for i in res:
            print(i)
            # 矩形を描画
            img.draw_rectangle(i.rect(), color = (255, 0, 0), thickness = 2)
    # 画像をLCDに描画
    lcd.display(img)

# モデルを開放
kpu.deinit(task)

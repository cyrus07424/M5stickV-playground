#
# バックライト2.
#

##################################################
# import
##################################################
import lcd
import time
import pmu

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init(color = lcd.WHITE)
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

##################################################
# main
##################################################
# axp192オブジェクトを取得
axp = pmu.axp192()

level = 0
while True:
    # バックライトの輝度を変更
    level = (level + 1) % 16
    axp.setScreenBrightness(level)
    # LCDに輝度を描画
    lcd.draw_string(lcd.width() // 2, lcd.height() // 2, "level: %2d" % level)
    # 1秒待機
    time.sleep(1)

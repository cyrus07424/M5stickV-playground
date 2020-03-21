#
# スプラッシュスクリーン.
#

##################################################
# import
##################################################
import lcd
import sensor
import image
import audio
from machine import I2C
from Maix import I2S, GPIO
from fpioa_manager import *

##################################################
# constants
##################################################
# 表示するロゴ画像ファイルのパス
image_filename = "/flash/startup.jpg"
# 再生する音声ファイルのパス
sound_filename = "/flash/ding.wav"

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

# I2Cデバイスを設定
i2c = I2C(I2C.I2C0, freq = 100000, scl = 28, sda = 29)
devices = i2c.scan()
time.sleep_ms(10)
print("i2c", devices)

# レジスタを設定
fm.register(board_info.SPK_SD, fm.fpioa.GPIO0)
fm.register(board_info.SPK_DIN, fm.fpioa.I2S0_OUT_D1)
fm.register(board_info.SPK_BCLK, fm.fpioa.I2S0_SCLK)
fm.register(board_info.SPK_LRCLK, fm.fpioa.I2S0_WS)

# GPIO設定
spk_sd = GPIO(GPIO.GPIO0, GPIO.OUT)

# スピーカーを有効化
spk_sd.value(1)

# 再生デバイスを設定
wav_dev = I2S(I2S.DEVICE_0)

##################################################
# function
##################################################
# 音声ファイルを再生
def play_sound(filename):
    try:
        # 音声ファイルを読み込み
        player = audio.Audio(path = filename)
        # 音量を設定
        player.volume(100)
        # 再生情報を取得
        wav_info = player.play_process(wav_dev)
        wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER, resolution = I2S.RESOLUTION_16_BIT, align_mode = I2S.STANDARD_MODE)
        wav_dev.set_sample_rate(wav_info[1])
        # 再生
        while True:
            ret = player.play()
            if ret == None:
                break
            elif ret == 0:
                break
        player.finish()
    except:
        pass

# バックライトの輝度を設定
# 0～8の9段階で指定
def set_backlight(level):
    level = min(level, 8)
    level = max(level, 0)
    val = (level + 7) << 4
    i2c.writeto_mem(0x34, 0x91, int(val))

# ロゴ画像を表示
def show_logo(image_filename, sound_filename):
    try:
        # 画像を読み込み
        img = image.Image(image_filename)
        # バックライトの輝度を設定
        set_backlight(0)
        # 画像をLCDに描画
        lcd.display(img)
        # バックライトの輝度を徐々に変更
        for i in range(9):
            set_backlight(i)
            time.sleep(0.1)
        # 音声ファイルを再生
        play_sound(sound_filename)
    except:
        lcd.draw_string(lcd.width() // 2 - 100, lcd.height() // 2 - 4, "Error: Cannot find %s" % image_filename, lcd.WHITE, lcd.RED)

##################################################
# main
##################################################
# ロゴ画像表示
show_logo(image_filename, sound_filename)

while True:
    # カメラ画像を取得
    img = sensor.snapshot()
    # 画像をLCDに描画
    lcd.display(img)

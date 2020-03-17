#
# WAV音声ファイルを再生.
#

##################################################
# import
##################################################
import sensor
import audio
from Maix import I2S, GPIO
from fpioa_manager import *

##################################################
# initialize
##################################################
# レジスタを設定
fm.register(board_info.SPK_SD, fm.fpioa.GPIO0)
fm.register(board_info.SPK_DIN, fm.fpioa.I2S0_OUT_D1)
fm.register(board_info.SPK_BCLK, fm.fpioa.I2S0_SCLK)
fm.register(board_info.SPK_LRCLK, fm.fpioa.I2S0_WS)

# GPIO設定
spk_sd = GPIO(GPIO.GPIO0, GPIO.OUT)
# GPIOを有効化
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
        wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT, align_mode = I2S.STANDARD_MODE)
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

##################################################
# main
##################################################
# 再生する音声ファイルのパス
file_name = "/flash/ding.wav"
try:
    while True:
            # 音声ファイルを再生
            play_sound(file_name)
            # 1秒待機
            time.sleep(1)
except:
    sys.exit()

#
# タイマー(MODE_PERIODIC).
#

##################################################
# import
##################################################
import time
from machine import Timer

##################################################
# function
##################################################
def on_timer(timer):
    print("time up:",timer)
    print("param:",timer.callback_arg())

##################################################
# main
##################################################
# 時間を指定(秒)
period = 1
unit = Timer.UNIT_S

# タイマーを設定
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode = Timer.MODE_PERIODIC, period = period, unit = unit, callback = on_timer, arg = on_timer, start = False, priority = 1, div = 0)

# タイマーの時間をコンソールに出力
print("period:", tim.period())

# タイマーを開始
tim.start()

# タイマーを停止
time.sleep(5)
tim.stop()

# タイマーを再開
time.sleep(5)
tim.restart()

# タイマーを停止
time.sleep(5)
tim.stop()

# オブジェクトを削除
del tim

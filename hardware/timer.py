#
# タイマー(MODE_ONE_SHOT).
#

##################################################
# import
##################################################
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
# 時間を指定(ミリ秒)
period = 3000

# タイマーを設定・開始
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode = Timer.MODE_ONE_SHOT, period = period, callback = on_timer, arg = on_timer)

# タイマーの時間をコンソールに出力
print("period:", tim.period())

#
# スレッド(3スレッド同時実行).
#

##################################################
# import
##################################################
import _thread
import time

##################################################
# function
##################################################
def func(name):
    while True:
        print("hello {}".format(name))
        time.sleep(1)

##################################################
# main
##################################################
# スレッドを作成
# M5stiackVは2コアのため3スレッド以上の同時実行を行うと実行順序のばらつきが大きくなる
_thread.start_new_thread(func,("1",))
_thread.start_new_thread(func,("2",))
_thread.start_new_thread(func,("3",))

# NOP
while True:
    pass

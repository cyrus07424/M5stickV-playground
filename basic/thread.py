#
# スレッド.
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
    while 1:
        print("hello {}".format(name))
        time.sleep(1)

##################################################
# main
##################################################
# スレッドを作成
_thread.start_new_thread(func,("1",))
_thread.start_new_thread(func,("2",))

# NOP
while 1:
    pass

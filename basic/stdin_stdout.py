#
# コンソールの入出力.
#

##################################################
# import
##################################################
import sys

##################################################
# main
##################################################
# 環境情報を表示
print("implementation:", sys.implementation)
print("platform:", sys.platform)
print("path:", sys.path)
print("Python version:", sys.version)

# コンソールからの入力を受け付ける
print("please input string, end with Enter")
r = sys.stdin.readline()

# 入力された文字列をコンソールに表示
w_len = sys.stdout.write(r)

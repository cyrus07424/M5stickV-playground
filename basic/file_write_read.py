#
# ファイルを書き込み・読み込み.
#

##################################################
# import
##################################################
import sys

##################################################
# main
##################################################
# ファイル名
filename = "my_file.txt"

# ファイルポインタを開く
f = open(filename, "w")

# ファイルに内容を書き込み
f.write("Hello M5stickV!")

# ファイルポインタを閉じる
f.close()

# ファイルポインタを開く
f = open(filename, "r")

# ファイルの内容を読み込み
content = f.read()

# ファイルの内容をコンソールに出力
print(content)

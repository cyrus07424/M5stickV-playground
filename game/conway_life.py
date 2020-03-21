#
# Conway's game of life.
#

##################################################
# import
##################################################
import gc
import lcd
import image
import random
from Maix import GPIO
from fpioa_manager import fm
from board import board_info

##################################################
# constants
##################################################
# セルの幅
CELL_WIDTH = 10
# セルの高さ
CELL_HEIGHT = 10
# X方向のセル数
X_MAX = lcd.width() // CELL_WIDTH
# Y方向のセル数
Y_MAX = lcd.height() // CELL_HEIGHT

##################################################
# initialize
##################################################
# メモリを開放
gc.mem_free()

# LCDを初期化
lcd.init()
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

# レジスタを設定
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)

# GPIO設定
button_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)

##################################################
# function
##################################################
# セルを初期化
def initialize():
    print("initialize")
    for x in range(X_MAX):
        for y in range(Y_MAX):
            cells[x, y] = False
    for x in range(X_MAX // 4, (X_MAX * 3) // 4):
        for y in range(Y_MAX // 4, (Y_MAX * 3) // 4):
            cells[x, y] = random.choice([True, False])

# ステップ
def step():
    print("step")
    neighbors = {}
    for x in range(1, X_MAX - 1):
        for y in range(1, Y_MAX - 1):
            count = -cells[x, y]
            for h in [-1, 0, 1]:
                for v in [-1, 0, 1]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count
    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            cells[cell] = True

##################################################
# main
##################################################
# ボタン押下中フラグ
button_a_pressed = 0

# セル
cells = {}

# セルを初期化
initialize()

while True:
    # Aボタンが押された場合
    if button_a.value() == 0 and button_a_pressed == 0:
        button_a_pressed = 1
    # Aボタンが放された場合
    if button_a.value() == 1 and button_a_pressed == 1:
        # セルを初期化
        initialize()
        button_a_pressed = 0
    # ステップ
    step()
    # 画像を作成
    img = image.Image()
    # 全てのセルに対して実行
    for (x, y), alive in cells.items():
        # 生きているセルの場合
        if alive:
            # 矩形を描画
            img.draw_rectangle(x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, fill = True, color = (0, 255, 0))
    # 画像をLCDに描画
    lcd.display(img)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import sys
# 入力を分割してリストにする
input_data = sys.stdin.read().split()

#x,yを整数として取得
x = int(input_data[0])
y = int(input_data[1])

#塩分の量を計算 xg * y% = 塩分の量
result = x * y // 100

#結果の出力
print(result)
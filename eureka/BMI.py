import sys
# 標準入力からデータを読み込み、改行で分割
#input_data = sys.stdin.read().split()

#体重と身長を取得
height = float(input()) #cm なら / 100
weight = float(input())
#BMIの目標値
target_BMI = float(input())

count = 0

#BMIの目標値をカウントする
while True:
    BMI = weight / (height ** 2)  #BMIを計算 BMI = 体重(kg) / 身(m)長 ** 2
    if BMI <= target_BMI:
        break
    weight -= 1  
    count += 1

#BMIの目標値との差を出力
print(count) 
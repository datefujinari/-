#目標体重 = 目標BMI × 身長²

#現在体重 - 目標体重

#すでに０の場合は表示なし
while weight > 0:
    bmi = weight / (height ** 2)
    if bmi <= target_BMI:
        break
    weight -= 1
    count += 1

#for文 解答（100点コード）
for w in range(int(weight), -1, -1):
    bmi = w / (height ** 2)
    if bmi <= target_BMI:
        break
    count += 1

#指示を受けつつテキストを表示
height = float(input("身長を入力してください(m): "))
weight = float(input("体重を入力してください(kg): "))
target_BMI = float(input("目標のBMIを入力してください: "))

#結果にもテキストを入れる場合
print(f"目標のBMIを達成するには{count}kg減量する必要があります。")
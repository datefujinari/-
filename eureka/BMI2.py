height = float(input())
weight = float(input())
target_BMI = float(input())

count = 0

for w in range(int(weight), -1, -1):
    bmi = w / (height ** 2)
    if bmi <= target_BMI:
        break
    count += 1

print(count)
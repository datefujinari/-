import sys

#入力の読み込み
apple_price = sys.stdin.read()
#N円のりんご
N = int(apple_price)
#３つ買う
ans = N * 3

print(ans)
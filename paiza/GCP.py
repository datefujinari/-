import sys
#すべてのデータを読み込み分割
# input_data[0] に N、それ以降にグーチョキバーを入れる。
input_data = sys.stdin.read().split()

# データがからの場合終了
if not input_data:
    sys.exit()
    #return def main()など使う場合

# １行目をN（回数）として取得
N = int(input_data[0])

#勝利数カウント
win_count = 0

#ジャンケンの手を２つずつ取り出して判定
#インデックスを２つずつ進める
for i in range(N):
    #アリスとボブの手を取得
    #[0]はNなので1からスタート
    #A = input_data[i * 2 -1]
    A = input_data[1 + i * 2]
    #B = input_data[i * 2]
    B = input_data[2 + i * 2]
    
    #アリスが勝つパターン
    if (
        (A == 'G' and B == 'C') or 
        (A == 'C' and B == 'P') or 
        (A == 'P' and B == 'G')
   ):
       win_count += 1
       
print(win_count)
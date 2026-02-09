import sys

def main():
    # 1. 商品データの定義
    items = {
        "1": {"name": "Cola", "price": 120},
        "2": {"name": "Tea", "price": 150},
        "3": {"name": "Water", "price": 100}
    }
    
    # 受け入れ可能な金額
    ALLOWED_MONEY = {10, 50, 100, 500, 1000}
    
    total_deposit = 0
    selected_items_total = 0

    # 2. 入力処理 (標準入力から1行ずつ読み込む)
    # 入力例の想定:
    # 100
    # 50
    # buy 1
    # buy 2
    # end
    
    for line in sys.stdin:
        command = line.strip().split()
        if not command:
            continue
            
        action = command[0]

        if action == "end":
            break
            
        # 入金処理
        if action.isdigit():
            money = int(action)
            if money in ALLOWED_MONEY:
                total_deposit += money
                print(f"投入金額合計: {total_deposit}円")
            else:
                print(f"エラー: {money}円は受け付けられません。")

        # 商品選択処理
        elif action == "buy":
            item_id = command[1]
            if item_id in items:
                price = items[item_id]["price"]
                # 残高チェック
                if total_deposit >= (selected_items_total + price):
                    selected_items_total += price
                    print(f"{items[item_id]['name']}を選択しました。")
                else:
                    print("エラー: 残高が足りません。")
            else:
                print("エラー: 無効な商品番号です。")

    # 3. お釣り計算と最終出力
    change = total_deposit - selected_items_total
    print("--- 最終結果 ---")
    print(f"購入合計額: {selected_items_total}円")
    print(f"お釣り: {change}円")

if __name__ == "__main__":
    main()
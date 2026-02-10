import sys

def main():
    # 商品データ
    items = {
        "1": {"name": "コーラ", "price": 120},
        "2": {"name": "お茶", "price": 150},
        "3": {"name": "水", "price": 100}
    }
    ALLOWED_MONEY = {10, 50, 100, 500, 1000}
    
    total_deposit = 0
    selected_items_total = 0

    print("--- 自動販売機システム (練習用) ---")
    print("コマンド例: '100', '500' (入金) / 'buy 1' (購入) / 'end' (終了)")
    print("----------------------------------")

    while True:
        # ターミナルからの入力を待機
        try:
            line = input("> ") 
        except EOFError:
            break

        command = line.strip().split()
        if not command:
            continue
            
        action = command[0]

        if action == "end":
            break
            
        # 入金処理 (数字のみが入力された場合)
        if action.isdigit():
            money = int(action)
            if money in ALLOWED_MONEY:
                total_deposit += money
                print(f"現在の投入金額合計: {total_deposit}円")
            else:
                print(f"エラー: {money}円は使用できません。")

        # 商品選択処理 ("buy 1" の形式)
        elif action == "buy":
            if len(command) < 2:
                print("エラー: 商品番号を指定してください（例: buy 1）")
                continue
                
            item_id = command[1]
            if item_id in items:
                price = items[item_id]["price"]
                # 残高チェック (投入金額から、これまでに選んだ合計を引いた額と比較)
                if (total_deposit - selected_items_total) >= price:
                    selected_items_total += price
                    print(f"{items[item_id]['name']} を排出しました。")
                else:
                    print(f"エラー: 残高不足です（あと {price - (total_deposit - selected_items_total)}円必要）")
            else:
                print("エラー: 存在しない商品番号です。")
        else:
            print("エラー: 無効なコマンドです。")

    # 最終結果
    change = total_deposit - selected_items_total
    print("\n--- 会計結果 ---")
    print(f"投入総額: {total_deposit}円")
    print(f"購入合計: {selected_items_total}円")
    print(f"お釣り  : {change}円")
    print("ありがとうございました！")

if __name__ == "__main__":
    main()
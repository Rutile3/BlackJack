import random

#変数宣言
#関数定義
def make_deck():
    suits = ['S', 'H', 'D', 'C']
    ranks = range(1, 13+1)
    deck = [(x, y) for x in ranks for y in suits]
    print(deck)
    random.shuffle(deck)
    return deck

def main():
    print(make_deck())
    player_money = 0 #あと書き直す
    while player_money > 0:
        pass
        #変数の初期化
        #ベット額の選択
        #お互いにカードを二枚づつ引く
        #プレーヤーのターン
        #ディーラーのターン
        #手札公開
        #勝敗判定
    #gameover

if __name__ == '__main__':
    main()
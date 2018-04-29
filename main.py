import random

#変数宣言
#関数定義
def make_deck():
    suits = ['S', 'H', 'D', 'C']
    ranks = range(1, 13+1)
    deck = [(x, y) for x in ranks for y in suits]
    random.shuffle(deck)
    return deck

def main():
    player_money = 100 #とりあえずこの値で
    while player_money > 0:
        player_hand = []
        dealer_hand = []
        deck = make_deck()
        for i in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        #ベット額の選択
        #お互いにカードを二枚づつ引く
        #プレーヤーのターン
        #ディーラーのターン
        print(player_hand)
        print(dealer_hand)
        #勝敗判定
        break # でバック用のループ抜け出し
    #gameover

if __name__ == '__main__': #直接実行されたときのみ実行
    main()
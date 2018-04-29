import random

RANK, SUIT = 0, 1

def GetPoint(hand):
    result = 0
    for card in hand:
        if card[RANK] > 10:
            num = 10
        else:
            num = card[RANK]
        result += num
    return result

def MakeDeck():
    suits = ['S', 'H', 'D', 'C']
    ranks = range(1, 13+1)
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    return deck

def main():
    player_money = 100 #とりあえずこの値で
    while player_money > 0:
        player_hand = []
        dealer_hand = []
        deck = MakeDeck()
        for i in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        #ベット額の選択
        #お互いにカードを二枚づつ引く
        #プレーヤーのターン
        #ディーラーのターン
        print(player_hand)
        print(GetPoint(player_hand))
        print(dealer_hand)
        print(GetPoint(dealer_hand))
        #勝敗判定
        break #デバッグ用のループ抜け出し
    #gameover

if __name__ == '__main__': #直接実行されたときのみ実行
    main()
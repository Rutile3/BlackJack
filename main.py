import random

RANK, SUIT = 0, 1

def GetPoint(hand):
    result = 0
    have_ace = False        #この変数名どうやろ？

    for card in hand:
        if card[RANK] == 1:
            if have_ace == True:
                input()
            have_ace = True
        if card[RANK] > 10: #絵札
            num = 10
        else:
            num = card[RANK]#1とここで1として加算する
        result += num
    if have_ace and result <=11:
        result += 10        #本来Aは11か1として扱うが既に1加算しているので10加算している

    return result

def MakeDeck():
    suits = ['S', 'H', 'D', 'C']
    ranks = range(1, 13+1)
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)

    return deck

def PrintPlayerHand(player_hand):
    print('プレーヤー(', GetPoint(player_hand), ')')
    for card in player_hand:
        print('[', card[SUIT], card[RANK], ']')
    print()#改行用

def main():
    player_money = 100 #とりあえずこの値で
    while player_money > 0:
        player_hand = []
        dealer_hand = []
        deck = MakeDeck()
        for i in range(3):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        PrintPlayerHand(player_hand)
        PrintPlayerHand(dealer_hand)
        #ベット額の選択
        #お互いにカードを二枚づつ引く
        #プレーヤーのターン
        #ディーラーのターン
        #手札公開
        #勝敗判定
        break #デバッグ用のループ抜け出し
    #gameover

if __name__ == '__main__': #直接実行されたときのみ実行
    main()
import random

RANK, SUIT = 0, 1

def GetPoint(hand):
    result = 0
    have_ace = False        #この変数名どうやろ？

    for card in hand:
        if card[RANK] == 1:
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

def PrintDealerHand(dealer_hand, show_all):
    if show_all:
        print('ディーラー(', GetPoint(dealer_hand), ')')
    else:
        print('ディーラー(', '##', ')')

    show_one = True
    for card in dealer_hand:
        if show_one or show_all:#ポーカー用語とは関係ない
            print('[', card[SUIT], card[RANK], ']')
            show_one = False    #1枚目のみ表示の場合はこれで2以降は表示になうようにする
        else:
            print('[', '# #', ']')
    print()#改行用
    
def PrintPlayerHand(player_hand):
    print('プレーヤー(', GetPoint(player_hand), ')')
    for card in player_hand:
        print('[', card[SUIT], card[RANK], ']')
    print()#改行用

def DealerTurn(deck, player_hand, dealer_hand):
    while GetPoint(player_hand) <= 21:
        if GetPoint(dealer_hand) >= 17:
            print('ディーラー：スタンド\n')
            break
        else:
            print('ディーラー：ヒット')
            dealer_hand.append(deck.pop())
        PrintDealerHand(dealer_hand, False)
      
def PlayerTurn(deck, player_hand, op):
    doubled, ending = False, False
    if op == '1':
        print('プレーヤー：スタンド\n')
        doubled, ending = False, True
    elif op == '2':
        print('プレーヤー：ヒット')
        player_hand.append(deck.pop())
        PrintPlayerHand(player_hand)
        doubled, ending = False, False
    elif op == '3':
        if len(player_hand) == 2:
            print('プレーヤー：ダブル')
            player_hand.append(deck.pop())
            PrintPlayerHand(player_hand)
            doubled, ending = True, True
        else:
            print('ダブルはできません')
    
    if GetPoint(player_hand) > 21:
        print('プレーヤーはバーストした!')
        ending = True
    elif GetPoint(player_hand) == 21:
        print('ブラックジャック!')
        ending = True

    return doubled, ending
    
def WinLose(dealer_hand, player_hand, bet, player_money):
    player_point = GetPoint(player_hand)
    dealer_point = GetPoint(dealer_hand)
    if player_point > 21:
        return 'プレーヤーの負け', player_money
    #この時点でディーラーがバーストしたらプレーヤーの勝ちが確定する
    if (player_point > dealer_point) or (dealer_point) > 21:
        if  player_point == 21:
            return 'プレーヤーの勝ち', player_money + int(bet * 2.5)
        else:
            return 'プレーヤーの勝ち', player_money + bet * 2
    elif player_point == dealer_point:
            return 'プッシュ', player_money + bet
    else:
        return 'プレーヤーの負け', player_money 

def main():
    turn = 1
    player_money = 100 #とりあえずこの値で
    deck = MakeDeck()

    while player_money > 0:
        player_hand = []
        dealer_hand = []
        print('-'*20)
        print('ターン：' + str(turn))
        print('所持金：' + str(player_money))
        print('-'*20)

        #ベット額の選択
        try:
            bet = int(input('ベット額 > '))
        except:
            print('整数で入力してください')
            continue
        if bet > player_money:
            print('所持金が不足しています')
            continue
        if bet <= 0:
            print('ベットできる額は1以上です')
            continue
        player_money -= bet

        #お互いに2枚ずつ引く
        if len(deck) < 10:
            deck = MakeDeck()
        for i in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        print('-'*20)
        PrintPlayerHand(player_hand)
        PrintDealerHand(dealer_hand, False)
        print('-'*20)

        #プレーヤーのターン
        while True:
            op = input('スタント：1, ヒット： 2, ダブル：3 > ')
            doubled, ending = PlayerTurn(deck, player_hand, op)
            if doubled:
                player_money -= bet
                bet *= 2
            if ending:
                break

        #ディーラーのターン
        DealerTurn(deck, player_hand, dealer_hand)

        #手札表示
        print('-'*20)
        PrintPlayerHand(player_hand)
        PrintDealerHand(dealer_hand, True)
        print('-'*20)

        #勝敗判定
        message, player_money = WinLose(dealer_hand, player_hand, bet, player_money)
        print(message)
        turn += 1

    print('所持金：' + str(player_money))
    print('GameOver')

if __name__ == '__main__': #直接実行されたときのみ実行
    main()
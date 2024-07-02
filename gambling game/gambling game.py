import random
import os

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing=True


#classes
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    def __str__(self):
        dec=''
        for card in self.all_cards:
            dec+='\n'+card.__str__()
        return 'deck is'+dec
    def grab_one_card(self):
        return self.all_cards.pop()


class Hand:
    def __init__(self):
        self.ace=0
        self.value=0
        self.cards=[]
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.ace+=1
    def firefist_ace(self):
        while self.value>21 and self.ace>=1:
            self.value-=10
            self.ace-=1

class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet





def take_bet():
    bet="heii"
    while bet.isdigit()==False:
        bet=input("enter the bet you r going to put:")
        if bet.isdigit()==False:
            print("Enter valid value")
          
    return int(bet)

def hit(deck,hand):
    hand.add_card(deck.grab_one_card())
    hand.firefist_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        scam=input("hit or stand:")
        scam.lower()
        if scam=='hit':
            return hit(deck,hand)
        elif scam=='stand':
            playing=False
        else:
            print('try again')
            continue
        break

def show_some(player,dealer):
    print("Dealers Hand:")
    print("First card hidden!")
    print(dealer.cards[1])
    print("")
    print("player's hand:") 
    for card in player.cards:
        print(card)
    print("")


def show_all(player,dealer):
    print("Dealers Hand:")
    for card in dealer.cards:
        print(card)
    #print("")
    print(f'total count is {dealer.value}')
    print("")
    print("player's hand:") 
    for card in player.cards:
        print(card)
    print("")

def player_busts(chips):
    print("player lost the bet")
    chips.lose_bet()

def player_wins(chips):
    print("player won the bet")
    chips.win_bet()

def dealer_busts(chips):
    print("dealer lost")
    chips.win_bet()

def dealer_wins(chips):
    print("dealer won")
    chips.lose_bet()

def push(chips):
    print("tie!push")

print("Welcome to BlackJack game\nRules are according to classic BlackJack game")
print("this game is designed for only 1 player against computer if needed can changed to multiple player vs the computer\nRules:")
print("U place the bet if you win the bet u get bet amount doubled and added to you Acc else u loose ur bet amount")
print("Intially u will be given 2 cards and dealer will be given 2 cards:and acording to sum of value of your cards u can hit or stand")
print("if your sum value is higher than 21 u busts and loose ur bet else u can continue to hit or stand")
print("if you hit the card ,card will be added to your sum ,if sum is less than 21 then youwill be shown one of the cards of dealer first card will be hidden")
print("if you choose stand ,dealers card will be revealed and his count he will be hit until its greater than or equal to your sum value")
print("after hiting if dealers sum value is greater than 20 you win dealer busts else you loose the game")
#print("So assuming you r clear with the game rules")
print("BONUS YOU WILL GIVEN 100 DOLLARS U CAN PLACE BET ANY AMOUNT FROM IT ACCORDINGLY U CAN PLAY THE GAME")
print("if you bet 10 from 100 then \n100-10=90\nyou win your balence will be 110(100+10*2) \nelse valence will be 90")
car="hoi"
print("")
while car not in["Y","N","y","n"]:
    car=input("do you wanna play the game Y or N:")
    #car.upper()
if car=='Y' or car=='y':
 hanger=True
else :
 hanger=False
chips=Chips()
while hanger:
    #chips=Chips()
    os.system('cls')
    if chips.total<=0:
     print("Your game ends here as your balance is not sufficient for making bet to play the game run the game again")
     break
    print(f"your current balence: {chips.total}")
    chips.bet=take_bet()
    while chips.bet>chips.total:
        print("you cannot bet amount greater than your balance")
        chips.bet=take_bet()
    
    os.system('cls')
    player=Hand()
    dealer=Hand()
    deck=Deck()
    deck.shuffle()
    player.add_card(deck.grab_one_card())
    player.add_card(deck.grab_one_card())
    dealer.add_card(deck.grab_one_card())
    dealer.add_card(deck.grab_one_card())
    print(f"player's value: {player.value}")
   # print(player.value)
    while playing:
       
        hit_or_stand(deck,player)
        os.system('cls')
        if playing:
         show_some(player,dealer)
         print(f"player's value: {player.value}")
        #print(player.value)
        if player.value>=21:
            player_busts(chips)
            print('bet amount lost:',chips.total)
            break
        elif playing==False:
            show_all(player,dealer)
            while dealer.value<=player.value:
                hit(deck,dealer)
           # print("")

            print("So after stand call\ndealer's hand:")
            for card in dealer.cards:
                print(card)
            print("")
            if dealer.value>20:
                dealer_busts(chips)
                print("")
                print('amount left:',chips.total)
                break
            elif dealer.value>player.value:
                dealer_wins(chips)
                print("")
                print('amount left:',chips.total)
                break

    tot=input('do you want to play again Y or N :')
    ans=tot.upper()
    if ans=='Y':
        hanger=True
        playing=True
    elif ans=='N':
        hanger=False
    else:
        print("valid input")
        
            
                
        
        
            













    
        






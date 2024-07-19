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
        bet=input("Enter the bet you r going to put:")
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

print("Game Rules:\nInitial Setup:\nYou start with $100.\nPlace a bet, which can be any amount up to your current balance.")
print("Card Dealing:\nBoth you and the dealer receive two cards.\nYour cards are both face-up.\nThe dealer has one card face-up and one card face-down.")
print("Gameplay:\nBased on the sum of your cards, you can choose to 'Hit' or 'Stand.'\nIf you 'Hit,' you receive an additional card.")
print("If the sum of your cards exceeds 21, you bust and lose your bet.\nIf the sum is 21 or less, one of the dealer's cards is revealed.")
print("If you 'Stand,' the dealer's hidden card is revealed.")
print("The dealer will continue to 'Hit' until their sum is equal to or greater than your sum.")
print("If the dealer's sum exceeds 21, the dealer busts, and you win.")
print("If the dealer's sum is equal to or higher than your sum without busting, you lose the game.")
print("Winning and Losing:")
print("If you win, your bet amount is doubled and added to your balance.\nIf you lose, your bet amount is deducted from your balance.")
print("Example:\nStarting balance: $100.You place a $10 bet.If you win, your balance becomes $120 ($100 + $10 * 2).If you lose, your balance becomes $90 ($100 - $10).Enjoy the game!")
car="hoi"
print("")
while car not in["Y","N","y","n"]:
    car=input("Do you wanna play the game Y or N:")
    if car not in["Y","N","y","n"]:
        print("invalid")
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
    print(f"Your current balence: {chips.total}")
    chips.bet=take_bet()
    while chips.bet>chips.total:
        print("You cannot bet amount greater than your balance")
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
            print('Balance remaining:',chips.total)
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
                print('Balance remaining:',chips.total)
                break
            elif dealer.value>player.value:
                dealer_wins(chips)
                print("")
                print('Balance remaining:',chips.total)
                break
    tot = "xxx"
    while tot not in["Y","N","y","n"]:
        tot=input("Do you wanna play the game Y or N:")
        if tot not in["Y","N","y","n"]:
            print("invalid")
    #tot=input('Do you want to play again Y or N :')
    ans=tot.upper()
    if ans=='Y':
        hanger=True
        playing=True
    elif ans=='N':
        hanger=False
    else:
        print("valid input")
        
            
                
        
        
            













    
        






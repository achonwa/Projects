import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

Playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

    
#creating the deck of object of cards containg the suits and ranks together    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deckpile = ""
        for card in self.deck:
            deckpile +=  "\n" + card.__str__()
        return "The deck pile has:  " + deckpile

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

    
    
    
    
    
#creating the hands of the computer and the player
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        
        self.cards.append(card)
        self.value += values[card.rank]
        
        
        #track aces
        if card.rank == "Ace":
            self.aces += 1
        
         
    
    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

            
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total+= self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
        
        
def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("Enter your bet amount: "))
            
        except:
            print("Sorry enter it in digits")
            
        else:
            if chips.bet > chips.total:
                print(f"You do not have enough Chips!! You have {chips.total}")
                
            else:
                break

                
                
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
    
def hit_or_stand(deck,hand):
    
    
    global Playing
    
    while True:
        
        x = input("Hit or stand enter value; h or s")
        
        if x[0].lower() == "h":
            hit(deck,hand)
            
        elif x[0].lower() == "s":
            print("Player will stand, Dealers Turn")
            Playing = False
            
        else:
            print("I do not understand, Enter value h or s!")
            continue
        break
        
        
def show_some(player,dealer):
    
    print("\n Dealer's Hand")
    print("First card is Hidden")
    print(dealer.cards[1])
    
    print("\n Players hand")
    for card in player.cards:
        print(card)
        
        

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
    
    

    
    
def player_busts(player,dealer,chips):
    print("BUST PLAYER")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player Wins!!")
    chips.win_bet()
    

def dealer_busts(player,dealer,chips):
    print("Player Wins! Dealer Busted!!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player Tie!! PUSH!!")
    
    
    

    
while True:
    
    deck = Deck()
    deck.shuffle()
    
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    #set player chips
    player_chips = Chips()
    
    #take bet
    
    take_bet(player_chips)
    
    #show cards but hid one of the dealers 
    
    show_some(player_hand, dealer_hand)
    
    while Playing:
        
        # asks player to hit or stand
        hit_or_stand(deck,player_hand)
        
        #show cards but hides one of the dealers 
        show_some(player_hand, dealer_hand)
        
        #if player hand exceeds 21 loses and breaks loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            
            break
            
            
            
      #if player hasnt busted play dealers hand until 17      
    if player_hand.value <= 21:
        
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
            
            
            #show all cards
        show_all(player_hand,dealer_hand)
        
        
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)
            
            
            
            #inform player total chips left
            
            
    print(f"\n Player Total chips are at: {player_chips.total}")
    
    #ask to play again
    
    new_game = input("Would you like to play another hand? y/n")
    
    if new_game[0].lower() == "y":
        Playing = True
        continue
        
    else:
        print("THANK YOU FOR PLAYING")
        
        break
    

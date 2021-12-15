'''
Blackjack Game
'''
import random
import war

suits = war.suits
ranks = war.ranks
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Deck:
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(war.Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0  
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
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
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?\n"))
        except:
            print("Please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"You do not have enough chips!\nCurrently you have: {chips.total} Chips")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  
    while True:
        x = input("Hit or Stand?(h/s)\n")
        if x[0].lower() == 'h':
            hit(deck,hand)
            break
        elif x[0].lower() == 's':
            print("Player Stands! Dealer's turn!")
            playing = False
            break
        else:
            print("Please enter h or s only!")
            continue

def show_some(player,dealer):
    print("Dealer's Hand:")
    print(f"Card 1: hidden!\nCard 2: {dealer.cards[1]}")
    print("\nPlayer's Hand:",*player.cards,sep='\n')
    
def show_all(player,dealer):
    print("Dealer's Hand:",*dealer.cards,sep='\n')
    print(f"Dealer Value: {dealer.value}")
    print("\nPlayer's Hand:",*player.cards,sep='\n')
    print(f"Player Value: {player.value}")

def player_busts(chips):
    print("Player BUSTED!")
    chips.lose_bet()

def player_wins(chips):
    print("Player WINS!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer BUSTED! Player Wins!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer WINS!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player TIE!")

def blackjack_start():
    global playing
    while True:
        print("WELCOME TO BLACKJACK!")
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    
        player_chips = Chips()
        take_bet(player_chips)
        show_some(player_hand,dealer_hand)

        while playing: 
            hit_or_stand(deck,player_hand)
            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_busts(player_chips)
                break
            
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
            
            show_all(player_hand,dealer_hand)
                    
            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()

        print(f"Player's Total Chips are: {player_chips.total}")
        
        new_game = input("Do you want to play again?(yes/no)\n")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break

if __name__ == '__main__':
    blackjack_start()
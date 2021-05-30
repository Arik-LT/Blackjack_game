import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 
        'Eight': 8,'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 
        'Ace': 11}
playing = True

class Card():  # suit rank and value
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " +deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()    
        return single_card

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card passed in from created deck uding deck.deal
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# function for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print ("sorry please provide an interger")
        else:
            if chips.bet > chips.total:
                print ("Sorry you do not have enough chips! You have: {}".format(chips.total))
            else:
                break

# function for taking hits, player can tak hits until bust
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Hit or Stand? Enter h or s ")
        if x.lower() == "h":
            hit(deck,hand)

        elif x.lower() == "s":
            print("player stands, dealer's turn")
            playing = False
        
        else:
            print("sorry please try again")
            continue
        break

# functions to display cards
def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass


# functions to handle end of game scenarios
def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

# Game Loop

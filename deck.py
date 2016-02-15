# Card Deck object
#
# Goal: construct a deck of cards without forgetting how classes work in python
#       - make games and stuff if it works
#
# Maxwell Tung
# 8.21.2015

import random

class CardDeck:
    def __init__(self):
        self.deck = []
        for i in range (1, 14):
            self.deck.append((i,'H'))
            self.deck.append((i,'D'))
            self.deck.append((i,'C'))
            self.deck.append((i,'S'))
        self.deck_size = 52
        self.suits = { 'H': ' of Hearts',
                       'D': ' of Diamonds',
                       'C': ' of Clubs',
                       'S': ' of Spades'}
        self.values = { 1: 'Ace',
                        2: '2',
                        3: '3',
                        4: '4',
                        5: '5',
                        6: '6',
                        7: '7',
                        8: '8',
                        9: '9',
                        10: '10',
                        11: 'Jack',
                        12: 'Queen',
                        13: 'King' }
        self.small_values = { 1: 'A',
                              2: '2',
                              3: '3',
                              4: '4',
                              5: '5',
                              6: '6',
                              7: '7',
                              8: '8',
                              9: '9',
                              10: 'T',
                              11: 'J',
                              12: 'Q',
                              13: 'K' }
        self.shuffle()

    def add_card(self, card):
        self.deck.append(card)
        self.deck_size += 1

    def get_val(self, card):
        return self.values[card[0]]

    def get_num(self, card):
        return card[0]

    def get_suit(self, card):
        return card[1]

    def get_color(self, card):
        if card[1] == 'H' or card[1] == 'D':
          return 'Red'
        else:
          return 'Black'
        
    def get_deck_size(self):
        return self.deck_size
    
    def get_card(self):
        selected_card = self.deck[0]
        del self.deck[0]
        self.deck_size -= 1
        return selected_card

    def shuffle(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for i in self.deck:
            self.show_card(i)
    
    def see_card(self, card):
        return(self.small_values[card[0]]+card[1])
    
    def see_full_card(self, card):
        return(self.values[card[0]]+self.suits[card[1]])

#print('\033[93m'+' color')
#print('\033[93m'+' secondcolor')

'''
myDeck = CardDeck()
print(myDeck.get_deck_size())
print( 'Your card is the: ')
myDeck.show_card(myDeck.get_card())
print( myDeck.get_deck_size())
'''

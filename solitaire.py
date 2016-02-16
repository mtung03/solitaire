# Lets try to make a game with these cards
#
# wish me luck
# Maxwell Tung
# 8.21.2015

import deck
import string
import os


class Solitaire:
    def __init__(self):
        self.mydeck = deck.CardDeck()
        self.foundations = [[],[],[],[]]
        self.tableau = [[],[],[],[],[],[],[]]
        self.waste = []
        self.wasteSize = 0
        self.user_vals = {}
        self.tableau_blacked = {'e':0, 'f': 0, 'g': 1, 'h': 2, 'i': 3, 'j': 4, 'k': 5, 'l': 6}
        self.red_suits = ['D', 'H']
        self.black_suits = ['C', 'S']

        
        # map each letter to the right "stack" 
        for j in range(0, 4):
            self.user_vals[string.ascii_lowercase[j]] = self.foundations[j]
        for j in range(4, 5):
            self.user_vals[string.ascii_lowercase[j]] = self.waste
        i = 6
        for j in range(5, 12):
            self.user_vals[string.ascii_lowercase[j]] = self.tableau[i]
            i -= 1

        self.deal()
        self.play_game()

    def play_game(self):
        while not self.has_won():
            #os.system('cls')
            self.display_full()
            user_move = input('Move? ')
            if not (self.check_move(user_move)):
                continue
            self.make_move(user_move)
            print(self.wasteSize)
        print("YOU WIN!!!")

    def make_move(self, move):
        if move == 'n':
            self.new_waste()
        elif move[0] == 'e':
            self.waste_move(move)
        else:            
            self.normal_move(move)

    def waste_move(self, move):
        self.wasteSize -= 1
        if self.wasteSize == 0:
            self.wasteSize = 3
        self.normal_move(move)

    def normal_move(self, move):
        aindex = move[0]
        size = move[1]
        bindex = move[2]
        if len(move) == 4:
            size = int( move[1] + move[2] )
            bindex = move[3]
        start_val = int(size) - 1
        start_stack = self.user_vals[aindex]
        end_stack = self.user_vals[bindex]

        if start_val == 0:
            moving_card = start_stack.pop() 
            if self.user_vals[aindex] in self.tableau and self.tableau_blacked[aindex] > 0 \
            and self.tableau_blacked[aindex] == len(self.user_vals[aindex]) :
                self.tableau_blacked[aindex] -= 1
            end_stack.append(moving_card)
        elif start_val < len(start_stack):
            temp_stack = []
            if self.user_vals[aindex] in self.tableau and self.tableau_blacked[aindex] > 0 :
                self.tableau_blacked[aindex] -= 1
            for i in range(start_val+1):
                temp_stack.append(start_stack.pop())
            for j in range(start_val+1):
                end_stack.append(temp_stack.pop())

    def check_move(self, move):
        if move == 'n':
            return True
        if len(move) < 3 or len(move) > 4:
            print("wrong input length")
            return False
        aindex = move[0]
        size = move[1]
        bindex = move[2]
        if not move[1].isdigit():
            print("invalid number input")
            return False
        if len(move) == 4:
             size = int(move[1]+move[2])
             bindex = move[3]
        start_val = int(size) - 1
        if (self.user_vals[aindex] not in self.tableau and self.user_vals[aindex] != self.waste) or len(self.user_vals) < 1:
            print('invalid startstack')
            return False
        if (self.user_vals[bindex] not in self.tableau) and (self.user_vals[bindex] not in self.foundations) and (self.user_vals[bindex] != self.waste):
            print('invalid endstack')
            return False
        if start_val < 0 or start_val > len(self.user_vals[aindex]) - self.tableau_blacked[aindex]:
            print('not enough cards')
            return False
        if len(self.user_vals[bindex]) == 0:
            print( bindex )
            print( self.user_vals[bindex] )
            if (self.user_vals[bindex] in self.tableau) and \
            self.mydeck.get_val(self.user_vals[aindex][len(self.user_vals[aindex])-(start_val+1)]) != 'King':
                print('only king on empty')
                return False
        elif self.user_vals[bindex] in self.tableau:
            if self.mydeck.get_num(self.user_vals[aindex]\
                [len(self.user_vals[aindex])-(start_val+1)]) \
                != self.mydeck.get_num(self.user_vals[bindex][len(self.user_vals[bindex])-1])-1:
                print("must be sequential")
                return False
            if self.mydeck.get_color(self.user_vals[aindex]\
                [len(self.user_vals[aindex])-(start_val+1)]) \
                == self.mydeck.get_color(self.user_vals[bindex][len(self.user_vals[bindex])-1]):
                print("must alternate color")
                return False
        elif self.user_vals[bindex] in self.foundations:
                return self.test_foundation_move(move, aindex, bindex)

        return True

    def test_foundation_move(self, move, aindex, bindex):
        if move[1] != '1':
            print("only one card on foundations")
            return False
        # must start a foundation with an ace
        if len(self.user_vals[bindex]) == 0:
            if not self.mydeck.get_num(self.user_vals[aindex][len(self.user_vals[aindex])-1]) == 1:
                return False
            return True
        else:
            # must be increasing sequencially and of the same suit
            if not (self.mydeck.get_num(self.user_vals[aindex][len(self.user_vals[aindex])-1]) == \
                   self.mydeck.get_num(self.user_vals[bindex][len(self.user_vals[bindex])-1]) + 1 \
                   and self.mydeck.get_suit(self.user_vals[aindex][len(self.user_vals[aindex])-1])\
                   == self.mydeck.get_suit(self.user_vals[bindex][len(self.user_vals[bindex])-1])):
                   print("must be increasing and same suit")
                   return False
            return True

    def deal(self):
        count_downer = 7
        for i in range(0,7):
            for j in range(count_downer):
                self.tableau[i].append(self.mydeck.get_card())
            count_downer -= 1
        self.new_waste()
        self.tableau.reverse()

    def new_waste(self):
        if self.mydeck.get_deck_size() >= 3:
            for i in range(3):
                self.waste.append(self.mydeck.get_card())
            self.wasteSize = 3
        elif self.mydeck.get_deck_size() > 0:
            self.wasteSize = 0
            for i in range(self.mydeck.get_deck_size()):
                self.waste.append(self.mydeck.get_card())
                self.wasteSize += 1
        else:
            self.wasteSize = 0
            for i in range(len(self.waste)):
                recarder = self.waste.pop()
                self.mydeck.add_card(recarder)
  
    def display_full(self):
        print(' a   b   c   d   e')
        foundation_line = ''
        for i in self.foundations:
            if len(i) > 0:
                foundation_line += '('+self.mydeck.see_card(i[len(i)-1])+')'
            else:
                foundation_line += '(  )'
        foundation_line += '('
        iterat = self.wasteSize
        for i in range(len(self.waste)-1,len(self.waste)-4, -1):
            if i >= 0 and iterat > 0:
                foundation_line += self.mydeck.see_card(self.waste[i])
            else:
                foundation_line += '  '
            if i > len(self.waste)-3:
                foundation_line += '|'
            iterat -= 1
        foundation_line += ')'
        print(foundation_line)
        print( ' f   g   h   i   j   k   l')
        for i in range(self.find_max_tableau()):
            this_line = ''
            for j in range(7):
                if i < len(self.tableau[j]):
                    if i >= self.tableau_blacked[string.ascii_lowercase[j+5]]:
                        this_line += '('+self.mydeck.see_card(self.tableau[j][i])+')'
                    else:
                        this_line += '(XX)'
                else:
                    this_line += '    '
            print(this_line)

    def find_max_tableau(self):
        curr_max = 0
        for i in self.tableau:
            if len(i) > curr_max:
                curr_max = len(i)
        return curr_max

    def has_won(self):
        return (len(self.foundations[0])== 13 and len(self.foundations[1])== 13 and len(self.foundations[2]) == 13 and len(self.foundations[3]) == 13)




letsplay = Solitaire()
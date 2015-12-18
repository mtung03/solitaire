# Lets try to make a game with these cards
#
# wish me luck
# Maxwell Tung
# 8.21.2015

import deck
import string


class Solitaire:
	def __init__(self):
		self.mydeck = deck.CardDeck()
		self.foundations = [[],[],[],[]]
		self.tableau = [[],[],[],[],[],[],[]]
		self.waste = []
		self.user_vals = {}
		self.tableau_blacked = [0,1,2,3,4,5,6]
		self.red_suits = ['D', 'H']
		self.black_suits = ['C', 'S']
		j = 0
		for i in string.ascii_lowercase:
			if j >= 12:
				break
			self.user_vals[i] = j
			j += 1
		self.deal()
		self.play_game()

	def play_game(self):
		while not self.has_won():
			tLength = 0
			for i in self.tableau:
				tLength += len(i)
			length = len(self.foundations[0])+len(self.foundations[1])+\
			len(self.foundations[2])+len(self.foundations[3])
			self.display_full()
			user_move = input('Move? ')
			self.make_move(user_move)
		print("YOU WIN!!!")

	def make_move(self, move):
		if move == 'n':
			self.new_waste()
		elif len(move) > 3 or len(move) < 1:
			print('a1')
			self.bad_move()
		elif move[0] == 'e':
			self.waste_move(move)
		elif self.check_normal(move):
			self.normal_move(move)
		else:
			print('a2')
			self.bad_move()

	def waste_move(self, move):
		if move[1] != '1':
			print('a3')
			self.bad_move()
		else:
			self.normal_move(move)

	def check_normal(self, move):
		if move[2] == 'a' or move[2] == 'b' or\
		   move[2] == 'c' or move[2] == 'd':
			if move[1] != '1':
				return False
			else:
				return True
		else:
			return True

	def normal_move(self, move):
		start_val = int(move[1])-1
		if move[0] == 'a' or move[0]=='b'or move[0]=='c' or \
		   move[0]=='d' or move[0] not in self.user_vals:
			print('invalid move a')
			self.make_move(input('Move? '))
			return ' '
		elif self.user_vals[move[0]] == 4:
			start_stack = self.waste
		elif self.user_vals[move[0]] >= 5 and self.user_vals[move[0]] < 12:
			start_stack = self.tableau[self.user_vals[move[0]]-5]
		else:
			print('invalid move b')
			self.make_move(input('Move? '))
			return ' '
		if self.user_vals[move[2]] in range(0,4):
			end_stack = self.foundations[self.user_vals[move[2]]]
		elif self.user_vals[move[2]] in range(5,12):
			end_stack = self.tableau[self.user_vals[move[2]]-5]
		else:
			print('invalid move c')
			self.make_move(input('Move? '))
			return ' '
		if start_val == 0:
			moving_card = start_stack.pop()
			end_stack.append(moving_card)
		elif start_val < len(start_stack):
			temp_stack = []
			for i in range(start_val+1):
				temp_stack.append(start_stack.pop())
			for j in range(start_val+1):
				end_stack.append(temp_stack.pop())
		else:
			print('invalid move d')
			self.make_move(input('Move? '))
			return
		if (start_stack in self.tableau) and (self.tableau_blacked[self.user_vals[move[0]]-5] > 0) and self.tableau_blacked[self.user_vals[move[0]]-5]  == len(start_stack):
			self.tableau_blacked[self.user_vals[move[0]]-5] -= 1

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
		elif self.mydeck.get_deck_size() > 0:
			for i in range(self.mydeck.get_deck_size()):
				self.waste.append(self.mydeck.get_card())
		else:
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
		for i in range(len(self.waste)-1,len(self.waste)-4, -1):
			if i >= 0:
				foundation_line += self.mydeck.see_card(self.waste[i])
			else:
				foundation_line += '  '
			if i > len(self.waste)-3:
				foundation_line += '|'
		foundation_line += ')'
		print(foundation_line)
		print( ' f   g   h   i   j   k   l')
		for i in range(self.find_max_tableau()):
			this_line = ''
			for j in range(7):
				#print(str(i) + ' ' +str(len(self.tableau[j])) + ' ' + str(self.tableau_blacked[j]))
				if i < len(self.tableau[j]):
					if i >= self.tableau_blacked[j]:
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

	def bad_move(self):
		print('invalid move e')
		self.make_move(input('Move? '))

	def has_won(self):
		return (len(self.foundations[0])== 13 and len(self.foundations[1])== 13 and len(self.foundations[2]) == 13 and len(self.foundations[3]) == 13)




letsplay = Solitaire()

import random

"""cards is a list of card values from 1 to 10. 
you can use any of the four basic math operations to get to target using the cards"""
def computes(cards, target):
	if len(cards)==1 and target==cards[0]:
		return repr(cards[0])

	for i in range(len(cards)):
		cards_copy = cards[:]
		this_card = cards_copy.pop(i)

		add = computes(cards_copy, round(target-this_card, 3))
		subtract_card = computes(cards_copy, round(target + this_card, 3))
		sub_from_card = computes(cards_copy, round(this_card - target, 3))
		mul = computes(cards_copy, round(target/this_card, 3))
		div = computes(cards_copy, round(target * this_card, 3))
		if add:
			return add + " + " + repr(this_card)
		elif subtract_card:
			return subtract_card + " - " + repr(this_card)
		elif sub_from_card:
			return repr(this_card) + " - (" + sub_from_card + ")"
		elif mul:
			return "(" + mul + ") * "  + repr(this_card)
		elif div:
			return "(" + div + ") / " + repr(this_card)

	return False

class FullDeck(object):
	def __init__(self):
		self.deck = [x for x in range(1, 11)]*4
	def draw_card(self):
		random_index = random.randrange(0, len(self.deck))
		random_card = self.deck.pop(random_index)
		return random_card
	def __repr__(self):
		return repr(self.deck)

class Hands(FullDeck):
	def __init__(self):
		deck = FullDeck()
		self.hand1 = [deck.draw_card() for i in range(20)]
		self.hand2 = deck.deck
	def __repr__(self):
		return "Player 1: " + repr(self.hand1) + "\nPlayer 2: " + repr(self.hand2)


def play():
	deck = FullDeck()
	cards = [deck.draw_card() for _ in range(4)]
	print("The following cards have been drawn: " + repr(cards))
	print("Try to make the number 24 out of these values using the four basic math operations.")
	user_answer = input("Is it possible? (y/n): ")
	answer = computes(cards, 24)

	while user_answer not in ['y', 'n']:
		user_answer = input('That is not a valid input. Please enter y or n: ')

	if not answer:
		if user_answer=='n':
			return "You're right. This is not possible!"
		else:
			return "Nope, this is not possible!"
	else:
		if user_answer=='n':
			trivial = input('There actually is a way to make 24! Can you think of it?')
		else:
			trivial = input('Are you ready to see a possible answer?')
		return 'The answer is ' + answer







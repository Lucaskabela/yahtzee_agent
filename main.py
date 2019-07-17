from random import randint

print("Starting the game of Yahtzee")

def turn_num():
	print("Turn Number: %d" % (turn))


class TurnState():

	def __init__(self):
		self.NUM_DICE = 5
		self.dice_roll = 0
		self.saved_dice = []

	def _num_to_roll(self):
		return self.NUM_DICE - len(self.saved_dice)

	def stop_turn(self):
		return dice_roll >= 3 or len(self.saved_dice) == self.NUM_DICE

	def roll_dice(self):
		self.dice_roll += 1
		just_rolled = []
		for die_num in range(self._num_to_roll()):
			just_rolled[die_num] = randint(1, 6)

		self.show_die(just_rolled)

	def show_die(self, just_rolled):
		print("        [ 1 2 3 4 5 ]\n")
		dice_str = []
		length = 0
		if len(self.saved_dice) > 0:
			dice_str.append("Saved:   ")
			for die in self.saved_dice:
				dice_str.append(" ")
				dice_str.append(str(die))
				length += 2
		dice_str.append("\n")
		if len(just_rolled) > 0:
			dice_str.append("rolled:  ")
			for _ in range(length):
				dice_str.append(" ")
			for die in just_rolled:
				dice_str.append(str(die))
				dice_str.append(" ")
			dice_str.append("\n")
		print(''.join(dice_str))

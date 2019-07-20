from random import randint

class ScoreRound():

    rows = ['s1', 's2', 's3', 's4', 's5', 's6', 'kind3', 'kind4',
            'full_house', 'sm_strt', 'lg_strt', 'yahtzee', 'chance',
            'bonus']

    rows_pretty = {
        's1': ['ones', 'one', '1s', '1'],
        's2': ['twos', 'two', '2s', '2'],
        's3': ['threes', 'three', '3s', '3'],
        's4': ['fours', 'four', '4s', '4'],
        's5': ['fives', 'five', '5s', '5'],
        's6': ['sixes', 'six', '6s', '6'],
        'kind3': ['three of a kind', '3 of a kind'],
        'kind4': ['four of a kind', '4 of a kind'],
        'full_house': ['full house'],
        'sm_strt': ['small straight', 'sm strt', 'sm straight', 'small strt',
                     'sm straight'],
        'lg_strt': ['large straight', 'lg strt', 'lg straight', 'large strt',
                     'lg straight'],
        'bonus': ['bonus yahtzee', 'yahtzee bonus']
    }

    def decode_row(field):
        field = field.lower()
        if field in ScoreRound.rows:
            return field
        for k in ScoreRound.rows_pretty.keys():
            if field in ScoreRound.rows_pretty[k]:
                return k
        if not field in ScoreRound.rows:
            print('Uhoh! "' + field + '" is not a row in our Score Card!')
            return None

    def row_pretty(field):
        field = ScoreRound.decode_row(field)
        if field in ScoreRound.rows_pretty.keys():
            return ScoreRound.rows_pretty[field][0].title()
        return field.title()

    def __init__(self, number=1):
        self.number = number
        for row in ScoreRound.rows:
            self.__dict__[row] = None

    def score(self):
        total = 0
        # Upper
        for i in range(1, 6):
            si = self.__dict__['s' + str(i)]
            if si is not None:
                total += si
        if total >= 63:
            total += 35

        # Lower
        for row in ['full_house', 'sm_strt', 'lg_strt', 'yahtzee', 'chance',
                    'bonus']:
            sl = self.__dict__[row]
            if sl is not None:
                total += sl

        return total

    def fill(self, field, score):
        field = ScoreRound.decode_row(field)
        if field is not None:
            if self.__dict__[field] is not None:
                print('Nice try! You\'ve already scored "' +
                      ScoreRound.row_pretty(field) + '"!')
            else:
                self.__dict__[field] = score
                return True 
        return False


class TurnState():

    def __init__(self):
        self.NUM_DICE = 5
        self.dice_roll = 0
        self.saved_dice = []

    def _num_to_roll(self):
        return self.NUM_DICE - len(self.saved_dice)

    def stop_turn(self):
        return self.dice_roll >= 3 or len(self.saved_dice) == self.NUM_DICE

    def roll_dice(self):
        self.dice_roll += 1
        print("Roll number %d" % (self.dice_roll))
        num_rolls = self._num_to_roll()
        just_rolled = [0] * num_rolls
        for die_num in range(num_rolls):
            just_rolled[die_num] = randint(1, 6)

        self.show_dice(just_rolled)
        indices = self.get_dice_to_save()
        self.save_rolled(just_rolled, indices)

    def show_dice(self, just_rolled):
        print("        [ 1 2 3 4 5 ]")
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
            dice_str.append("Rolled:   ")
            for _ in range(length):
                dice_str.append(" ")
            for die in just_rolled:
                dice_str.append(str(die))
                dice_str.append(" ")
            dice_str.append("\n")
        print(''.join(dice_str))

    def get_dice_to_save(self):
        nums = input("Enter the number of dice you want to save:  ")
        if nums is None or len(nums) == 0:
            return []
        num_arr = map(int, nums.split(" "))
        return [num for num in num_arr if num > len(self.saved_dice)]

    def save_rolled(self, just_rolled, indices):
        if self.dice_roll == 3:
            for die in just_rolled:
                self.saved_dice.append(die)
        else:
            for idx in indices:
                idx -= len(self.saved_dice) + 1
                dice_score = just_rolled[idx]
                just_rolled.remove(dice_score)
                self.saved_dice.append(dice_score)


def print_rules():
    print("~~~~~~~~Starting the game of Yahtzee~~~~~~~~\n")
    print("Okay, here are the rules: ")
    print("The game will roll all dice not saved for you.  Nice!")
    print("You will be prompted to save and unsave dice at the end of a roll")
    print("    Enter the indicies of dice you want to save seperated by spaces!")
    print("        eg: \"1 2 5\" will save the first, second, and 5th dice")
    print("          (provided they are not already saved!)")
    print("    Maximum of only 3 rolls per turn!")
    print("Your turn ends when you have saved all your dice, or after the 3rd roll")
    print("You will then enter your score into the field.  Scouts honor!")
    print("Game ends when you fill the score card.  Good Luck! \n\n")


def get_turn_score(test_turn):
    print("\nYour dice from that turn are: ")
    print(test_turn.saved_dice)
    field = input("Where do you want to put your points? ")
    pts = int(input("How many points should I put there? "))
    return field, pts


def turn_num(turn):
    print("\n~~~~~Turn Number: %d~~~~~" % (turn))


def main():
    print_rules()
    score = ScoreRound()
    turns = []
    while len(turns) < 13: 
        curr_turn = TurnState()
        turn_num(len(turns) + 1)
        while not curr_turn.stop_turn():
            curr_turn.roll_dice()
        
        field, pts = get_turn_score(curr_turn)
        while not score.fill(field, pts):
            field, pts = get_turn_score(curr_turn)

        turns.append(curr_turn)

    print("Game over, you got: " + str(score.score()))


if __name__ == '__main__':
    main()

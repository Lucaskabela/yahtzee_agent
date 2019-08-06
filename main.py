from random import randint


class ScoreRound():

    rows = [
        's1', 's2', 's3', 's4', 's5', 's6', 'kind3', 'kind4', 'full_house',
        'sm_strt', 'lg_strt', 'yahtzee', 'chance', 'bonus'
    ]

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
        'sm_strt': [
            'small straight', 'sm strt', 'sm straight', 'small strt',
            'sm straight'
        ],
        'lg_strt': [
            'large straight', 'lg strt', 'lg straight', 'large strt',
            'lg straight'
        ],
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
        for row in [
                'full_house', 'sm_strt', 'lg_strt', 'yahtzee', 'chance',
                'bonus'
        ]:
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

    def fill(self, field, dice):
        score = 0
        field = ScoreRound.decode_row(field)
        if field == 's1':
            # count the number of ones
            score = self.score_num(1, dice)
        elif field == 's2':
            score = self.score_num(2, dice)
        elif field == 's3':
            score = self.score_num(3, dice)
        elif field == 's4':
            score = self.score_num(4, dice)
        elif field == 's5':
            score = self.score_num(5, dice)
        elif field == 's6':
            score = self.score_num(6, dice)
        elif field == 'kind3':
            score = self.get_kind3_score(dice)
        elif field == 'kind4':
            score = self.get_kind4_score(dice)
        elif field == 'full_house':
            score = self.get_full_house_score(dice)
        elif field == 'sm_strt':
            score = self.get_sm_strt_score(dice)
        elif field == 'lg_strt':
            score = self.get_lg_strt_score(dice)
        elif field == 'yahtzee':
            score = self.get_yahtzee(dice)
        elif field == 'chance':
            score = sum(dice)

        if field is not None:
            if self.__dict__[field] is not None:
                print('Nice try! You\'ve already scored "' +
                      ScoreRound.row_pretty(field) + '"!')
            else:
                self.__dict__[field] = score
                print("Put %d points in %s" % (score, field))
                return True
        return False

    def score_num(self, number, dice):
        return sum(number for die in dice if die == number)

    def get_kind3_score(self, dice):
        num_same = [0] * 6
        for die in dice:
            num_same[die - 1] += 1
        return sum(
            dice) if 3 in num_same or 4 in num_same or 5 in num_same else 0

    def get_kind4_score(self, dice):
        num_same = [0] * 6
        for die in dice:
            num_same[die - 1] += 1
        return sum(dice) if 4 in num_same or 5 in num_same else 0

    def get_full_house_score(self, dice):
        num_same = [0] * 6
        for die in dice:
            num_same[die - 1] += 1
        return 25 if 3 in num_same and 2 in num_same else 0

    def get_sm_strt_score(self, dice):
        dice.sort()
        straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        for possible in straights:
            not_in = False
            for num in possible:
                if num not in dice:
                    not_in = True
            if not not_in:
                return 30
        return 0

    def get_lg_strt_score(self, dice):
        dice.sort()
        straights = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        for possible in straights:
            if possible == dice:
                return 40
        return 0

    def get_yahtzee(self, dice):
        num_same = [0] * 6
        for die in dice:
            num_same[die - 1] += 1
        return 50 if 5 in num_same else 0

    def display_score(self):
        #header = ['fields: |']
        #scores = ['scores: |']
        header = ['|']
        scores = ['|']

        width = 73
        for i in range(0, width):
            print('-', sep='', end='')
        print('')
        for field in self.rows:
            score = str(self.__dict__[field]
                        ) if self.__dict__[field] is not None else '---'
            header.append(' {0:^15s} |'.format(ScoreRound.row_pretty(field)))
            scores.append(' {0:^15s} |'.format(score))
            if len(''.join(header)) >= 80 or len(''.join(scores)) >= 80:
                print(''.join(header[:-1]))
                print(''.join(scores[:-1]))
                #width = len(''.join(header[:-1]))
                width = 73
                for i in range(0, width):
                    print('-', sep='', end='')
                print('')
                #header = ['fields: |', header[-1:][0]]
                #scores = ['scores: |', scores[-1:][0]]
                header = ['|', header[-1:][0]]
                scores = ['|', scores[-1:][0]]

        print(''.join(header))
        print(''.join(scores))
        width = len(''.join(header))
        for i in range(0, width):
            print('-', sep='', end='')
        print('')


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
        self.saved_dice += self.get_dice_to_save2(just_rolled)
        if self.dice_roll < 3:
            print("Saved: " + str(self.saved_dice))
            self.get_dice_to_unsave()

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

    def get_dice_to_save2(self, rolled):
        """
        Accepts `1 2 3` or `1, 2, 3`
        """
        roll_orig = rolled
        nums = input("Which dice do you want to save? ")
        if self.dice_roll == 3:
            for die in rolled:
                self.saved_dice.append(die)
            return []
        elif nums is None or len(nums) <= 0:
            return []

        nums = list(
            map(
                int, "".join(list(filter(lambda c: c in '0123456790 ',
                                         nums))).split(" ")))
        if len(nums) > 5 or len(nums) + len(self.saved_dice) > 5:
            print("You can't save that many!")
            return self.get_dice_to_save2(roll_orig)
        keeps = []

        def pop_member(dice):
            if dice in rolled:
                keeps.append(dice)
                rolled.remove(dice)
                return None
            else:
                print("You don't have any %ds!" % (dice))
                return self.get_dice_to_save2(roll_orig)

        for dice in nums:
            val = pop_member(dice)
            if val is not None:
                return val
        return keeps

    def get_dice_to_unsave(self):
        nums = input("Which dice do you want to unsave? ")
        if nums is None or len(nums) <= 0:
            return []
        nums = list(
            map(
                int, "".join(list(filter(lambda c: c in '0123456790 ',
                                         nums))).split(" ")))
        if len(self.saved_dice) < len(nums):
            print("You don't have that many dice!")
            return self.get_dice_to_save2(roll_orig)

        def pop_member(dice):
            if dice in self.saved:
                self.saved_dice.remove(dice)
                return None
            else:
                print("You don't have any %ds!" % (dice))
                return self.get_dice_to_unsave()

        for dice in nums:
            pop_member(dice)

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
    print(
        "    Enter the indicies of dice you want to save seperated by spaces!")
    print("        eg: \"1 2 5\" will save the first, second, and 5th dice")
    print("          (provided they are not already saved!)")
    print("    Maximum of only 3 rolls per turn!")
    print("Your turn ends when you have saved all your dice, or after the "
          "3rd roll")
    print("You will then enter your score into the field.  Scouts honor!")
    print("Game ends when you fill the score card.  Good Luck! \n\n")


def get_turn_score(test_turn):
    print("\nYour dice from that turn are: ")
    print(test_turn.saved_dice)
    field = input("Where do you want to put your points? ")
    # pts = int(input("How many points should I put there? "))
    return field


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

        field = get_turn_score(curr_turn)
        while not score.fill(field, curr_turn.saved_dice):
            field = get_turn_score(curr_turn)

        turns.append(curr_turn)
        score.display_score()

    print("Game over, you got: " + str(score.score()))


if __name__ == '__main__':
    main()

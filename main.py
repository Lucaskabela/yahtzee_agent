from random import randint

turn = 0
print("Starting the game of Yahtzee")

def turn_num():
	print("Turn Number: %d" % (turn))

def roll():
    return randint(1, 6)


class ScoreRound():

    rows = ['s1', 's2', 's3', 's4', 's5', 's6', 'kind3', 'kind4',
            'full_house', 'sm_strt', 'lg_strt', 'yahtzee', 'chance',
            'bonus']

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
        if not field in ScoreRound.rows:
            print('Uhoh! "' + field + '" is not a row in our Score Card!')
        elif self.__dict__[field] is not None:
            print('Nice try! You\'ve already scored "' + field + '"!')
        else:
            self.__dict__[field] = score

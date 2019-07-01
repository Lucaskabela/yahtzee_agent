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

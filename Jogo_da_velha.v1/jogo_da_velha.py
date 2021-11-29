class JogoDaVelha:
    def __init__(self):
        self.board = [[letter + str(num) for num in range(1, 4)] for letter in 'abc']
        self.simbol = ['X ', 'O ']
        self.available_positions = [self.board[listt][val] for listt in range(3) for val in range(3)]
        self.simb = 'X'
        self.player = 0

    def hashtag(self):
        for listt in self.board:
            for c1, v in enumerate(listt, 1):
                print(' ', v, '|' if c1 % 3 != 0 else f'\n{"-"*20}\n', end='')

    def change_turn(self):
        self.player = (self.player + 1) % 2
        self.simb = self.simbol[self.player].strip()

    def move(self, pos):
        line, column = 'abc'.index(pos[0]), int(pos[1])-1
        self.board[line][column] = self.simb
        self.available_positions.remove(pos)

    def victory(self):
        diagonals = [[self.board[li][co] for li, co in zip(range(3), range(2, -1, -1))],
                     [self.board[li][co] for li, co in zip(range(3), range(3))]]
        for line in self.board:
            if line.count(self.simb) == 3:
                return True
        for line in zip(*self.board):
            if line.count(self.simb) == 3:
                return True
        for line in diagonals:
            if line.count(self.simb) == 3:
                return True

        return False



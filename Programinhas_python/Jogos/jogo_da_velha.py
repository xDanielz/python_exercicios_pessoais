class JogoDaVelha:
    
    def __init__(self):
        self.position = [[] for _ in range(3)]
        for n, letter in enumerate(list('abc')):
            for num in range(3):
                self.position[n].append(letter+str(num+1))

        self.simbol = ['X ', 'O ']
        self.available_positions = [self.position[listt][val] for listt in range(3) for val in range(3)]
        self.player = 0

    def change_turn(self):
        self.player = (self.player+1) % 2

    def hashtag(self):
        for listt in self.position:
            for c1, v in enumerate(listt, 1):
                print(' ', v, '|' if c1 % 3 != 0 else f'\n{"-"*20}\n', end='')

    def move(self, pos):
        simb = self.simbol[self.player]
        indx = list('abc').index(pos[0])
        self.position[indx][int(pos[1])-1] = simb
        self.available_positions.remove(pos)

    def rules(self):
        simb = self.simbol[self.player]
           
        for c1 in range(3):
            count_of_xo = self.position[c1].count(simb)
            if count_of_xo == 3:
                return True
            
        r = 0
        for val in range(3):
            for listt in range(3):
                if self.position[listt][val] == simb:
                    r += 1
                    if r == 3:
                        return True
                else:
                    break
            r = 0

        rang = list(range(3))
        for _ in range(2):
            r = 0
            for k in rang:
                if self.position[k][k] == simb:
                    r += 1
                    if r == 3:
                        return True
                else:
                    break
            rang = list(range(2, -1, -1))
        return False

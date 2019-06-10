import random


class Game(object):
    def __init__(self):
        self.lup = (0, 0)
        self.width = 3
        self.height = 3
        self.matrix = list()
        self.GameWidth = 5
        self.GameHeight = 5


    def create_game_matrix(self):
        for i in range(5):
            row = list()
            for j in range(5):
                if j >= 2:
                    row.append(1)
                else:
                    row.append(0)
            self.matrix.append(row)

        arr = ['down', 'right', 'up', 'left']
        for a in range(len(arr)):
            rndnum = random.randint(0, self.width)
            for b in range(rndnum):
                self.move_border(arr[a])
                rot = random.randint(0, 5)
                for r in range(rot):
                    self.rotate_border()

        self.lup = (0, 1)


    def move_border(self, side):
        map = {
            'up': (self.lup[0] - 1, self.lup[1]),
            'down': (self.lup[0] + 1, self.lup[1]),
            'left': (self.lup[0], self.lup[1] - 1),
            'right': (self.lup[0], self.lup[1] + 1)
        }

        if side == 'up':
            if self.lup[0] > 0:
                self.lup = map[side]
        if side == 'down':
            if self.lup[0] + self.height - 1 < len(self.matrix) - 1:
                self.lup = map[side]
        if side == 'left':
            if self.lup[1] > 0:
                self.lup = map[side]
        if side == 'right':
            if self.lup[1] + self.width - 1 < len(self.matrix[0]) - 1:
                self.lup = map[side]


    def rotate_border(self):
        a = list()
        for i in range(self.lup[0], self.lup[0] + self.height):
            row = list()
            for j in range(self.lup[1], self.lup[1] + self.width):
                row.append(self.matrix[i][j])
            a.append(row)
        b = tuple(zip(*a[::-1]))
        i2 = 0
        j2 = 0
        for i1 in range(self.lup[0], self.lup[0] + self.height):
            for j1 in range(self.lup[1], self.lup[1] + self.height):
                self.matrix[i1][j1] = b[i2][j2]
                j2 += 1
            i2 += 1
            j2 = 0


    def getGameWidth(self):
        return self.GameWidth


    def getGameHeight(self):
        return self.GameHeight


    def __getitem__(self, key):
        return self.matrix[key[0]][key[1]]


    def getRect(self):
        return (self.lup, self.width, self.height)

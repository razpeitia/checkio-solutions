from collections import deque

class Chess(object):
    def __init__(self):
        self.board = [
            [0] * 8
            for i in range(8)
        ]
        self.start = None
        self.end = None

    def convert(self, pos):
        x, y = pos
        x, y =  ord(x) - ord('a'), int(y) - 1
        return (y, x)

    def is_valid(self, pos):
        i, j = pos
        return (0 <= i < 8) and (0 <= j < 8)

    def get_neighbors(self, pos):
        offset = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),

            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]
        i, j = pos
        neighbors = []
        for di, dj in offset:
            pos = i + di, j + dj
            if self.is_valid(pos):
                yield pos

    def get_non_visited_neighbors(self, pos):
        neighbors = self.get_neighbors(pos)
        for neighbor in neighbors:
            if not self.is_visited(neighbor):
                yield neighbor

    def is_visited(self, pos):
        i, j = pos
        return self.board[i][j] == 1

    def mark(self, pos):
        i, j = pos
        self.board[i][j] = 1

    def walk(self):
        queue = deque([(self.start, 0)])
        while queue:
            pos, length = queue.pop()
            self.mark(pos)
            if pos == self.end:
                return length
            else:
                for neighbor in self.get_non_visited_neighbors(pos):
                    self.mark(neighbor)
                    queue.appendleft((neighbor, length+1))

    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.board)


def checkio(move):
    """str -> int
    Number of moves in the shortest path of knight
    """
    board = Chess()
    start, end = map(board.convert, move.split('-'))
    board.start = start
    board.end = end

    ans = board.walk()
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"

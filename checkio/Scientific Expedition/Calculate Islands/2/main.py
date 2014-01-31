class World(object):
    WATER = 0
    EARTH = 1
    def __init__(self, world):
        self.world = world
        self.h = len(self.world)
        self.w = len(self.world[0])
        self.islands = []
        
    def is_valid(self, i, j):
        return (0 <= i < self.h) and (0 <= j < self.w)
    
    def flood_fill(self, i, j, target, replace, count=0):
        if self.world[i][j] == target:
            self.world[i][j] = replace
            count += 1
        
        pos = [( 1, -1), ( 1, 0), ( 1, 1),
               ( 0, -1),          ( 0, 1),
               (-1, -1), (-1, 0), (-1, 1),]
               
        for i_, j_ in pos:
            i__, j__ = i_ + i, j + j_
            if self.is_valid(i__, j__) and self.world[i__][j__] == target:
                count += self.flood_fill(i__, j__, target, replace)
        return count
        
    def get_islands(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.world[i][j] == self.EARTH:
                    size = self.flood_fill(i, j, self.EARTH, self.WATER)
                    self.islands.append(size)
        self.islands.sort()
        return self.islands
                    

def checkio(data):
    world = World(data)
    return world.get_islands()

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"


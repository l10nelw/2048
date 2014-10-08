import random

class Game:
    debug = False
    
    def __init__(self, size):
        """initialise board of a given size (an integer), adding some
        starting numbers"""
        self._board = [[0]*size for i in range(size)]
        self._size = size
        self._moved = False
        for i in range(int(size/2)): self._spawn([2])
        
    def _spawn(self, numlist):
        "spawn a number randomly chosen from a given list, at a random empty space"
        while True:
            x = random.randrange(self._size)
            y = random.randrange(self._size)
            if self._board[x][y] == 0:
                self._board[x][y] = numlist[0] if len(numlist) == 1 else random.choice(numlist)
                self._lastspawn = x, y # for debugging
                break
        
    def _flip(self):
        "flip board left to right"
        for row in self._board:
            row.reverse()
        
    def _rotate(self):
        "rotate board 90 degrees clockwise"
        self._board = [ list(row) for row in zip(*self._board[::-1]) ]
        
    def _unrotate(self):
        "rotate board 90 degrees counter-clockwise"
        self._board = [ list(row) for row in zip(*self._board) ][::-1]

    def _move(self):
        "move numbers across board to the left"
        for row in self._board:
            lus = 0 # leftmost unoccupied space 
            for i in range(self._size):
                if row[i]: # if a number occupies this space,
                    if i > lus: # if the number is to the right of the LUS,
                        # move it to the LUS
                        row[lus] = row[i]
                        row[i] = 0
                        self._moved = True
                    lus += 1 # LUS is now a step to the right
    
    def _merge(self):
        "merge identical adjacent numbers to the left"
        for row in self._board:
            for i in range(1, self._size): # check from the 2nd to 4th space
                if row[i] and row[i] == row[i-1]: # check the left adjacent space
                    row[i-1] *= 2
                    row[i] = 0
                    self._moved = True

    def _swipe(self):
        "basic swipe (left)"
        self._move()
        self._merge()
        self._move()

    def _endswipe(self):
        "complete a swipe thus: spawn a number and display the board"
        if self._moved:
            self._spawn([2,2,2,4])
            self.display()
            self._moved = False
        else:
            self.display()
        
    def display(self):
        """print board, and also print moved status and spawn location
        if self.debug is non-zero"""
        for row in self._board:
            print('\t'.join(str(num) if num else '·' for num in row))
            print()
        if self.debug:
            x, y = self._lastspawn
            print('moved =', self._moved, end='')
            print('  R{}C{} = {}'.format(x+1, y+1, self._board[x][y]) if self._moved else '')

    def left(self):
        "swipe left"
        self._swipe()
        self._endswipe()
        
    def right(self):
        "swipe right"
        self._flip()
        self._swipe()
        self._flip()
        self._endswipe()
        
    def down(self):
        "swipe down"
        self._rotate()
        self._swipe()
        self._unrotate()
        self._endswipe()

    def up(self):
        "swipe up"
        self._unrotate()
        self._swipe()
        self._rotate()
        self._endswipe()
        
import random

class Game:
	
	def __init__(self, size):
		"initialise board with a given size (an integer)"
		self.board = [[0]*size for i in range(size)]
		self.size = size
		self.moved = False
		self.lastspawn = 0, 0
		self.spawn([2])
		self.spawn([2])
		
	def spawn(self, numlist):
		"spawn a number randomly chosen from a given list, at a random empty space"
		while True:
			x = random.randrange(self.size)
			y = random.randrange(self.size)
			if self.board[x][y] == 0:
				self.board[x][y] = numlist[0] if len(numlist) == 1 else random.choice(numlist)
				self.lastspawn = x, y
				break
		
	def flip(self):
		"flip the board left to right"
		for row in self.board:
			row.reverse()
		
	def rotate(self):
		"rotate the board 90 degrees clockwise"
		self.board = [ list(row) for row in zip(*self.board[::-1]) ]
		
	def unrotate(self):
		"rotate the board 90 degrees counter-clockwise"
		self.board = [ list(row) for row in zip(*self.board) ][::-1]

	def move(self):
		"move numbers across the board to the left"
		for row in self.board:
			lus = 0 # leftmost unoccupied space 
			for i in range(self.size):
				if row[i]: # if a number occupies this space,
					if i > lus: # if the number is to the right of the LUS,
						# move it to the LUS
						row[lus] = row[i]
						row[i] = 0
						self.moved = True
					lus += 1 # LUS is now a step to the right
	
	def merge(self):
		"merge identical adjacent numbers to the left"
		for row in self.board:
			for i in range(1, self.size): # check from the 2nd to 4th space
				if row[i] and row[i] == row[i-1]: # check the left adjacent space
					row[i-1] *= 2
					row[i] = 0
					self.moved = True

	def swipe(self):
		"basic swipe (left)"
		self.move()
		self.merge()
		self.move()

	def endswipe(self):
		"complete the swipe thus: spawn a number and display the board"
		if self.moved:
			self.spawn([2,2,2,4])
			self.display()
			self.moved = False
		else:
			self.display()
		
	def display(self):
		"print the board, moved status and spawn location"
		for row in self.board:
			print('\t'.join(str(num) if num else '·' for num in row))
			print()
		x, y = self.lastspawn
		print('moved =', self.moved, end='')
		print('  R{}C{} = {}'.format(x+1, y+1, self.board[x][y]) if self.moved else '')

	def left(self):
		"swipe left"
		self.swipe()
		self.endswipe()
		
	def right(self):
		"swipe right"
		self.flip()
		self.swipe()
		self.flip()
		self.endswipe()
		
	def down(self):
		"swipe down"
		self.rotate()
		self.swipe()
		self.unrotate()
		self.endswipe()

	def up(self):
		"swipe up"
		self.unrotate()
		self.swipe()
		self.rotate()
		self.endswipe()



import itertools

# nagy, lyukas, szögletes, sötét

class Board:
	def __init__(self):
		self.mtx = []
		for i in range(4):
			self.mtx.append([None for _ in range(4)])
		self.pieces_left = list(itertools.product(*[[0,1] for y in range(4)]))
	
	def add_piece(self, x, y, piece):
		self.mtx[x][y] = piece
		self.pieces_left[self.pieces_left.index(piece)] = None
	
	def is_complete_line(self, lst):
		if any(x is None for x in lst):
			return False
		for z in zip(*lst):
			if all(x==0 for x in z) or all(x==1 for x in z):
				return True
		return False
	
	def is_over(self):
		for i, line in enumerate(self.mtx):
			if self.is_complete_line(list(line)):
				return set((i, j) for j in range(4))
		
		for j, line in enumerate(list(zip(*self.mtx))):
			if self.is_complete_line(list(line)):
				return set((i, j) for i in range(4))
		
		if self.is_complete_line([self.mtx[i][i] for i in range(4)]):
			return set((i,i) for i in range(4))
		
		if self.is_complete_line([self.mtx[i][4-i-1] for i in range(4)]):
			return set((i,4-i-1) for i in range(4))
		
		if all(piece is None for piece in self.pieces_left):
			s = set()
			for i in range(4):
				for j in range(4):
					s.add((i,j))
			return s
		
		return False
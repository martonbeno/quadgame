import tkinter as tk
from PIL import ImageTk, Image

from Board import *

class View:
	def __init__(self):
		
		path = ".\\images\\"
		
		root = tk.Tk()
                root.title("Quad game")
		root.geometry("800x600")
		
		self.bg_color = "saddle brown"
		root.configure(bg=self.bg_color)
		
		self.leftside = tk.Frame(master=root, width=250, height=400, bg=self.bg_color)
		self.rightside = tk.Frame(master=root, width=400, height=400, bg=self.bg_color)
		self.bottom = tk.Frame(master=root, width=100, height=100, bg=self.bg_color)
		
		self.leftside.grid(column=0, row=0, padx=20, pady=20)
		self.rightside.grid(column=1, row=0, padx=40, pady=20)
		self.bottom.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
		
		self.board = Board()
		
		self.small_images = dict()
		self.big_images = dict()
		for piece in self.board.pieces_left:
			img = Image.open(path + ''.join(str(i) for i in piece) + ".png")
			self.big_images[piece] = ImageTk.PhotoImage(img)
			self.small_images[piece] = ImageTk.PhotoImage(img.resize((50,50)))
		self.small_images[None] = ImageTk.PhotoImage(Image.open(path + "empty.png").resize((50,50)))
		self.big_images[None] = ImageTk.PhotoImage(Image.open(path + "empty.png"))
		
		self.new_game()
		
		root.bind("<Escape>", lambda e: root.destroy())
		
		root.mainloop()
	
	def new_game(self):
		self.board = Board()
		self.act_piece = None
		self.is_active = True
		self.highlighted_right = set()
		self.act_player = 0
		
		self.draw_leftside()
		self.draw_rightside()
		self.draw_bottom()
	
	def game_over(self, over):
		self.is_active = False
		self.highlighted_right = over
		self.draw_rightside()
		self.draw_bottom(game_over=True)
		print("vége")
	
	def select_piece(self, piece):
		def f():
			if not self.is_active:
				return
			if self.act_piece is not None:
				return
			if piece not in self.board.pieces_left:
				return
			if piece is None:
				return
			
			self.act_piece = piece
			self.act_player = (self.act_player + 1)%2
			self.draw_leftside()
			self.draw_bottom()
		return f
	
	def place_piece(self, x, y):
		def f():
			if not self.is_active:
				return
			if self.act_piece is None:
				return
			self.board.add_piece(x, y, self.act_piece)
			self.draw_rightside()
			self.draw_leftside()
			self.act_piece = None
			
			over = self.board.is_over()
			if over:
				self.game_over(over)
		return f
	
	def draw_bottom(self, game_over=False):
		if not game_over:
			text = f"Player {self.act_player+1}"
		else:
			if len(self.highlighted_right) == 16:
				text = "Draw."
			else:
				text = f"Player {self.act_player+1} won"
		try:
			self.label.grid_remove()
		except:
			pass
		self.label = tk.Label(self.bottom, text=text, font=("Helvetica", 24), fg="white", bg=self.bg_color)
		self.label.grid(row=0,column=0)
		if not self.is_active:
			self.new_game_button = tk.Button(self.bottom)
			self.new_game_button.config(text="new game", command=self.new_game)
			self.new_game_button.grid(row=1,column=0,pady=20)
		else:
			try:
				self.new_game_button.grid_remove()
			except:
				pass
		
	
	def draw_rightside(self):
		for i in range(4):
			for j in range(4):
				piece = self.board.mtx[i][j]
				img = self.big_images[piece]
				if piece is None:
					button = tk.Button(self.rightside)
					button.config(image=img, command=self.place_piece(i, j), bg=self.bg_color)
					button.grid(row=i, column=j)
				else:					
					label = tk.Label(self.rightside, image=img, background="yellow" if (i,j) in self.highlighted_right else None)
					label.grid(row=i, column=j)
	
	def draw_leftside(self):
		for i in range(4):
			for j in range(4):
				index = i*4+j
				piece = self.board.pieces_left[index]
				button = tk.Button(self.leftside)
				button.config(image=self.small_images[piece], command=self.select_piece(piece))
				if self.act_piece is not None and piece == self.act_piece:
					button.config(bg="yellow")
				button.grid(row=i, column=j)

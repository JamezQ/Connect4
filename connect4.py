from copy import deepcopy
class createboard(object):
	"""Create a blank connect4 board,\
 use player names and optional player peices"""
	def __init__(self,player1="player1",player2="player2",player1char="x",player2char="o"):
		self.won = False
		self.history = []
		
		self.player1char = player1char
		self.player2char = player2char
		# Check if inputted values are sane
		if len(self.player1char) == 1:
			pass
		else:
			self.player1char = "x"
		if len(self.player2char) == 1:
			pass
		else:
			self.player2char = "o"

		self.player1 = player1
		self.player2 = player2
		# Check if inputted values are sane
		if self.player1:
			pass
		else:
			self.player1 = "player1"
		if self.player2:
			pass
		else:
			self.player2 = "player2"
			
			
		self.turnchar = self.player1char
		self.turn = self.player1
		
		self.board = []
		for x in range(6):
			self.board.append(["|_"])
			for i in range(5):
				self.board[x].append("|_")
			self.board[x].append("|_|")
		
	def printboard(self):
		for row in range(6):
			print ''.join(self.board[row])+"\n",
		print "|=|=|=|=|=|=|=|\n[a","b","c","d","e","f","g]"
	def getboard(self):
		get = []
		for row in range(6):
			get.append(''.join(self.board[row])+"\n")
		get.append(' '.join(["|=|=|=|=|=|=|=|\n[a","b","c","d","e","f","g]"]))
		get = ''.join(get)
		return get
	def __checkplace__(self,row,column):
		outofrange = False
		if row > 5:
			outofrange = True
		elif row < 0:
			outofrange = True
		if column >6:
			outofrange = True
		elif column < 0:
			outofrange = True
		
		if outofrange:
			return False
			
		if "_" in self.board[row][column]:
			return True
		elif self.player1char in self.board[row][column]:
			return self.player1char
		elif self.player2char in self.board[row][column]:
			return self.player2char
	def __turnchar__(self):
		if self.turnchar == self.player1char:
			self.turnchar = self.player2char
			self.turn = self.player2
			return self.player1char
		elif self.turnchar == self.player2char:
			self.turnchar = self.player1char
			self.turn = self.player1
			return self.player2char
			
	def place(self,row):
		returndata = {}
		returndata['Victory'] = False
		if self.won:
			if self.won == ["Cat"]:
				returndata['Error'] = "Catsgame! No winner, no more possible"+\
				"moves!"
			else:
				returndata['Error'] = "The game has already been won by: "+self.won\
			+"."
		else:
			returndata['Error'] = None
			collet = ["a","b","c","d","e","f","g"]
			playerchar = self.__turnchar__()
			if row in collet:
				colnum = collet.index(row)
				rowcheck = 5
				while True:
					if self.__checkplace__(rowcheck,colnum) is True:
						self.board[rowcheck][colnum] = self.board[rowcheck][colnum].\
						replace("_",playerchar)
						player1vic = self.__checkvictory__(self.player1char)
						player2vic = self.__checkvictory__(self.player2char)
						if player1vic:
							self.won = self.player1
							returndata['Victory'] = self.player1
							self.board = player1vic
						elif player2vic:
							self.won = self.player2
							returndata['Victory'] = self.player2
							self.board = player2vic
						elif player1vic is None:
							returndata['Victory'] = ["Cat"]
							self.won = ["Cat"]
						break
					elif self.__checkplace__(rowcheck,colnum) is False:
						returndata['Error'] = "There is no room in that column."
						self.__turnchar__()
						break
					else:
						rowcheck -= 1
			else:
				returndata['Error'] = "That column does not exist."
				self.__turnchar__()
		return returndata
	def __checkvictory__(self,playerchar):
		"""Check all possible wins on the board return board with 
 winning pices in upper case, or return False if there is no victory"""
		victory = False
		boardx = deepcopy(self.board)
		row = 5
		column = 6
		starburst_bag = []
		cats_game = True
		for a in range(row+1):
			for b in range(column+1):
				starburst = []
				starburst.append((a,b))
				
				if self.__checkplace__(a,b) is True:
					cats_game = False
					continue
				elif self.__checkplace__(a,b) == playerchar:
					
					starburst.append(1)
					
					
					while True:
						if a-starburst[1] < 0:
							break
						if self.__checkplace__(a-starburst[1],b) == playerchar:
							starburst[1] += 1
						else:
							break
							
						
					starburst.append(1)
					
					while True:
						if a-starburst[2] < 0:
							break
						if b+starburst[2] > 6:
							break
						if self.__checkplace__(a-starburst[2],b+starburst[2])\
						 == playerchar:
							starburst[2] += 1
						else:
							break
					
					
					starburst.append(1)
					
					while True:
						if b+starburst[3] > 6:
							break
						if self.__checkplace__(a,b+starburst[3]) == playerchar:
							starburst[3] += 1
						else:
							break
					
					
					starburst.append(1)
					
					while True:
						if a+starburst[4] > 5:
							break
						if b+starburst[4] > 6:
							break
						if self.__checkplace__(a+starburst[4],b+starburst[4])\
						== playerchar:
							starburst[4] += 1
						else:
							break
						
						
					starburst_bag.append(starburst)
		
		for starburst in starburst_bag:
			
			a = starburst[0][0]
			b = starburst[0][1]
			
			if starburst[1] > 3:
				victory = True
				for i in range(starburst[1]):
					boardx[a-i][b] = boardx[a-i][b].\
					replace(playerchar,playerchar.upper())
			if starburst[2] > 3:
				victory = True
				for i in range(starburst[2]):
					boardx[a-i][b+i] = boardx[a-i][b+i].\
					replace(playerchar,playerchar.upper())
			if starburst[3] > 3:
				victory = True
				for i in range(starburst[3]):
					boardx[a][b+i] = boardx[a][b+i].\
					replace(playerchar,playerchar.upper())
			if starburst[4] > 3:
				victory = True
				for i in range(starburst[4]):
					boardx[a+i][b+i] = boardx[a+i][b+i].\
					replace(playerchar,playerchar.upper())
			
		if cats_game:
			return None
		if victory:
			return boardx
		else:
			return False
def main():
	player1 = raw_input('Enter player 1: ')
	player2 = raw_input('Enter player 2: ')
	
	board = createboard(player1,player2)
	lasterr = False
	while True:
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
		if lasterr:
			print lasterr
			
		board.printboard()
		row = raw_input("Player "+board.turn+"("+board.turnchar+")"+", enter row: ")
		a = board.place(row)
		if a['Error']:
			lasterr = a['Error']
		else:
			lasterr = False
		if a['Victory'] == ["Cat"]:
			print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
			board.printboard()
			print "Catsgame! No winners, no more possible moves. Play again."
			break
		elif a['Victory']:
			print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
			board.printboard()
			print "Congratulations",a['Victory']+", you win!"
			break
	#~ a = raw_input("play again?(yes/no)\n")
	#~ if "n" in a:
		#~ exit()
	#~ else:
		#~ main()
if __name__ == "__main__":
	main()

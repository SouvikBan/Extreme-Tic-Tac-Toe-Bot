import sys

class TEAM46:
    def __init__(self):
        self.position_weight  = ((3,2,3),(2,3,2),(3,2,3))
        self.boardHeuristics = {}                          
        self.blockHeuristics = {}
        self.max_depth = 3
        self.blockWin = 20 #number of points if a block is won by us 
        patterns = [] #winning patterns in block - will cotain position of flags in the winning pattern.

        #vertical and horiz patterns
        for i in xrange(3):
			row_array = [] # i'th row
			col_array = [] # i'th column
			for j in xrange(3):
				row_array.append((i,j))
				col_array.append((j,i))
			patterns.append(tuple(row_array))
			patterns.append(tuple(col_array))

        #diagonal patterns
        patterns.append(((0,0) , (1,1) , (2,2)))
        patterns.append(((0,2) , (1,1) , (2,0)))
        
        self.patterns = tuple(patterns)

    def oppFlag(self, flag):
		# NOT operation on flag
		return 'o' if flag == 'x' else 'x'

    def board_pattern_check(self, blockHeurs, array):
        #array - every winning pattern in patterns[]
        playerCount = 0
        patternHeur = 0
        for pos in array:
            val = blockHeurs[pos[0]][pos[1]]
            #blockHeurs is the value/score of a block that we calculated in block_pattern_check
            patternHeur += val
            if val < 0:
                return 0
            elif val == self.blockWin:
                playerCount += 1
        
        multiplier = 1.125
         #when zero block won by us - included in block contribution in board_heuristics
        if playerCount == 2:
            multiplier = 2.25
        
        return multiplier * patternHeur
    
    def block_pattern_check(self, block, array, flag):
        #array - every winning pattern in patterns[]
        flagCount = 0
        for pos in array:
			if block[pos[0]][pos[1]] == flag:
				flagCount += 1
            #1/3 will have only cell contribution written in Block_heuristics
			elif block[pos[0]][pos[1]] == self.oppFlag(flag):
                #if opponent's flag is present, discard
				return 0
        
        if flagCount == 2:
			#ƒ2/3 of pattern complete. some points awarded for this
			return 6 #calculate somepoints 

        return 0


    def board_heuristics(self,blockHeurs):
        # give boardHeurs for 1 block
        #partial board = 1.125* sum if 1, 2.25*sum if 2 , for 3 game over won
        #sum is sum of block values involved in the incomplete pattern = 1/8 * 1/4 * block_heuristics * position_weight    
        boardHeur = 0
        for i in xrange(3):
			for j in xrange(3):
				if blockHeurs[i][j] > 0:
					boardHeur += (self.position_weight[i][j] * blockHeurs[i][j])/32

        return boardHeur
    
    def heuristics(self, flag, board):
        #call pattern check with every pattern in patterns[] after which give cell contribution in blockHeurs
        #block won = 20, block lost = -1, partial block = cell weight(1)/2*maximum cell weight(2)
        pass    


    def Minimax(self, board, flag, depth, old_move, alpha , beta):
        
        checkGoal = board.find_terminal_state()
        if checkGoal[1] == 'WON':
			if checkGoal[0] == self.who:
				return float("inf")
			else:
				return float("-inf")
        elif checkGoal[1] == 'DRAW':
                return -100000

        validCells = board.find_valid_move_cells(old_move)
        
        if depth == self.max_depth:
            return self.heuristics(flag,board)
        
        maxMove = (flag == self.who)

        if maxMove:
            bestVal = float('-inf')
            for i in xrange(len(validCells)):

                cell = validCells[i]
                board.update(old_move, cell, flag)
                
                bestVal = max(bestVal, self.Minimax(board,self.oppFlag(flag), depth+1, cell , alpha, beta))
                alpha   = max( alpha, bestVal )
                
                board.big_boards_status[cell[0]][cell[1]] = '-'
                board.small_boards_status[cell[0]/3][cell[1]/3] = '-'
                
                if beta <= alpha:
                    break
                return bestVal
        else:
            bestVal = float('inf')
            for i in xrange(len(validCells)):
                
                cell = validCells[i]
                board.update(old_move, cell, flag)
                
                bestVal = min(bestVal, self.Minimax(board,self.oppFlag(flag), depth+1, cell , alpha, beta))
                beta    = min( beta, bestVal )
                
                board.big_boards_status[cell[0]][cell[1]] = '-'
                board.small_boards_status[cell[0]/3][cell[1]/3] = '-'

                if beta <= alpha:
                    break
                return bestVal

   
    def Move(self,board, old_move, flag):
        
        self.who = flag

        validCells = board.find_valid_move_cells(old_move)
        best_move = validCells[0]

        while True:
            best_move = self.Minimax(board,'MaxPlayer', 0 , old_move, float('-inf'), float('inf'))
            self.max_depth += 1
        
        return best_move


    
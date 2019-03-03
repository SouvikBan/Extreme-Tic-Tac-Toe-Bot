import sys

class TEAM46:
    def __init__(self):
        self.position_weight  = (3,2,3,2,3,2,3,2,3)
        self.boardHeuristics = {}                          
        self.blockHeuristics = {}
        self.who = 'MaxPlayer' #flag='x'
        self.blockPoints = 30 #number of points if a block is won by us 
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

    def board_pattern_check(self,board,flag):
        pass
    
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
			return somepoints #calculate somepoints 
		return 0
        # pass


    def board_heuristics(self,board):
        #call pattern check with every pattern in patterns[] after which give cell contribution
        #partial board = 1.125* sum if 1, 2.25*sum if 2 , for 3 game over won
        #sum is sum of block values involved in the incomplete pattern = 1/8 * 1/4 * block_heuristics * position_weight    
        pass
    
    def block_heuristics(self, block):
        #block won = 20, block lost = -1, partial block = cell weight(1)/2*maximum cell weight(2)
        block_heuristic_value = 0

        if block_pattern_check == 2:

        if self.block_pattern_check(block):
             
    
    def cell_heuristics(self,index): #1/8 of cell_weight
        return (self.position_weight[index]/8)






    def BestMove(self, board, flag, depth, old_move, maxDepth, alpha , beta):
        validCells = board.find_valid_move_cells(old_move)
        
        if depth == maxDepth:
            return self.board_heuristics(board)
        
        maxMove = (flag == self.who)

        if maxMove:
            bestVal = float('-inf')
            for child in xrange(len(validCells)):
                bestVal = max(bestVal, self.BestMove(board,'MinPlayer',depth+1, child , maxDepth, alpha, beta))
                alpha   = max( alpha, bestVal )
                if beta <= alpha:
                    break
                return bestVal
        else:
            bestVal = float('inf')
            for child in xrange(len(validCells)):
                bestVal = min(bestVal, self.BestMove(board,'MaxPlayer',depth+1, child , maxDepth, alpha, beta))
                beta    = min( beta, bestVal )
                if beta <= alpha:
                    break
                return bestVal

   
    
    
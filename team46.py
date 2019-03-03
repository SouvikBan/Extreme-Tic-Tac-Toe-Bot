import sys

class TEAM46:
    def __init__(self):
        self.position_weight  = (3,2,3,2,3,2,3,2,3)
        self.boardHeuristics = {}                          
        self.blockHeuristics = {}
        self.who = 'MaxPlayer'

    def board_pattern_check(self,board):
        pass
    
    def block_pattern_check(self,block):
        pass


    def board_heuristics(self,board):
        #partial board = 1.125* sum if 1, 2.25*sum if 2 , for 3 game over won
        #sum is sum of block values involved in the incomplete pattern = 1/8 * 1/4 * block_heuristics * position_weight    
        pass
    
    def block_heuristics(self, block):
        #block won = 20, block lost = -1, partial block = cell weight(1)/2*maximum cell weight(2)
        block_heuristic_value = 0

        if block_pattern_check == 2:

        if self.block_pattern_check(block):
             
    
    def cell_heuristics(self,index): #1/8 of weight_position
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

   
    def Move(self,board, old_move, flag):

        
    
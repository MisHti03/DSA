class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board)<1:
            return board
        r_len,c_len=len(board),len(board[0])
        
        for i in range(r_len):
            self.dfs(i,0,board)
            self.dfs(i,c_len-1,board)
        for j in range(c_len):
            self.dfs(0,j,board)
            self.dfs(r_len-1,j,board)
        
        for i in range(r_len):
            for j in range(c_len):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='I':
                    board[i][j]='O'
        
                
                    
    def dfs(self,row,col,board):
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!='O':
            return
        board[row][col]='I'
        self.dfs(row+1,col,board)
        self.dfs(row-1,col,board)
        self.dfs(row,col-1,board)
        self.dfs(row,col+1,board)
    
        
                
        
        
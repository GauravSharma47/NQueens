class NQueens:
    #initialise board with n*n; n being the constructor input
    def __init__(self,n):
        self.n=n
        self.board=list()
        for i in range(n):
            self.board.append([0]*n)
    def printboard(self):
        print(*self.board,sep="\n")
    def isSafe(self,row,column):
        #Only checking from left because plotting queens from left to right
        for i in range(column):
            if self.board[row][i]==1:
                return False
        #left up
        for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
            if self.board[i][j]==1:
                return False
        #left Down
        for i,j in zip(range(row,self.n,1),range(column,-1,-1)):
            if self.board[i][j]==1:
                return False
        return True
    def solve(self,row,column):
        if column>=self.n:
            return True
        for i in range(row,self.n):
            if self.isSafe(i,column):
                self.board[i][column]=1
                if self.solve(column+1)==True:
                    return True
                self.board[i][column]=0

        return False

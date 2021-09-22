import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]  
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
    
    def validate_move(self, player, column):
        if (self.game_result != ""):
            return "End Of Game"
        elif(self.remaining_moves <= 0):
            return "Out of Moves"    
        elif(self.current_turn != player):
            return "Not your turn"
        elif (column > 7 or column < 0):
            return "Out of Bounds"
        elif (self.board[0][column] != 0):
            return "Overflow"
        else:
            return "Valid"
           

    def add_chip(self, player, column):
        for row in range(5,-1,-1):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                break

        self.remaining_moves -= 1
        self.check_win(player, column, row)
        
        if (self.current_turn == 'p2'):
            self.current_turn = 'p1' 
        elif (self.current_turn == 'p1'):
            self.current_turn = 'p2'
        return

    def check_row(self, player, row):
        Row = self.board[row]
        if(Row.count(player) < 4):
            return False
        for c in range(0, 4):
            if (Row[c:c+4].count(player) == 4):
                return True
        return False
    
    def check_col(self, player, col, row):
        Col = [x[col] for x in self.board]
        if(Col.count(player) < 4):
            return False
        for c in range(0, 4):
            if (Col[c:c+4].count(player) == 4):
                return True
        return False

    def check_ndiag(self, player, col, row):
        x = row
        y = col
        Diag = []
        while(x > 0 and y > 0):
            x -= 1
            y -= 1
        while(x <= 5 and y <= 6):
            Diag.append(self.board[x][y])
            x += 1
            y += 1

        if(Diag.count(player) < 4):
            return False
        for c in range(0, 4):
            if (Diag[c:c+4].count(player) == 4):
                return True
        return False

    def check_pdiag(self, player, col, row):
        x = row
        y = col
        Diag = []
        while(x < 5 and y > 0):
            x += 1
            y -= 1
        while(x >= 0 and y <= 6):
            Diag.append(self.board[x][y])
            x -= 1
            y += 1

        if(Diag.count(player) < 4):
            return False
        for c in range(0, 4):
            if (Diag[c:c+4].count(player) == 4):
                return True
        return False

    def check_win(self, player, col, row):
        self.check_pdiag(player, col, row)
        self.check_ndiag(player, col, row)

        if(self.check_col(player, col, row) or self.check_row(player, row) 
        or self.check_pdiag(player, col, row) or self.check_ndiag(player, col, row)):
            self.game_result = player
            return True
        


        
        

'''
Add Helper functions as needed to handle moves and update board and turns
'''


    

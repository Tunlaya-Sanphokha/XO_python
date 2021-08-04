#6201012620040 คงเดช สมใจ 
#6201012620074 ณัฐชนน วะลับ 
#6201012620341 นางสาวตุลยา สารโพคา
gamerun = 1
class Board:
    def __init__(self):
        self.board_array = [['1','2','3'],['4', '5', '6'],['7', '8', '9']]
        self.player = "X"
        self.turn_count = 0
    
    def display_board(self,):
        print()
        for i in self.board_array:
            for j in i:
                print("|",end=' ')
                print(j,end=" ")
            print("|\n--------------")
        print()
    
    def change_player(self):
        if self.player =='X':
            self.player = 'O'
        else:
            self.player = 'X'

    def add_postion(self) :
        self.turn_count += 1
        while(True):
            print("Player: " + self.player) 
            inputNumber =  Input_Processor.input_checker()
            if inputNumber.isnumeric():
                realInput = int(inputNumber) - 1
                if (realInput <= 8 and realInput >= 0):
                    x = int(realInput%3)
                    y = int(realInput//3)
                    if self.board_array[y][x] != "X" and self.board_array[y][x] != "Y":
                        self.board_array[y][x] = self.player
                        return True
                    else :
                        print("Invalid Try Again")
                        return False
    
    def check_winner(self):
        global gamerun
        if self.board_array[0][0] == self.board_array[0][1] == self.board_array[0][2] != " ":
            self.display_board()
            print("Player " + self.board_array[0][1] + " Win!!")
            gamerun = 0

        elif self.board_array[1][0] == self.board_array[1][1] == self.board_array[1][2] != " " :
            self.display_board()
            print("Player " +self.board_array[1][1] + " Win!!")
            gamerun = 0

        elif self.board_array[2][0] == self.board_array[2][1] == self.board_array[2][2] != " ":
            self.display_board()
            print("Player " +self.board_array[2][1] + " Win!!")
            gamerun = 0

    #ชนะแนวตั้ง 
        elif self.board_array[0][0] == self.board_array[1][0] == self.board_array[2][0] != " ":
            self.display_board()
            print("Player " + self.board_array[1][0] + " Win!!")
            gamerun = 0

        elif self.board_array[0][1] == self.board_array[1][1] == self.board_array[2][1] != " ":
            self.display_board()
            print("Player " +self.board_array[1][1]+ " Win!!")
            gamerun = 0
            

        elif self.board_array[0][2] == self.board_array[1][2] == self.board_array[2][2] != " ":
            self.display_board()
            print("Player " + self.board_array[1][2] + " Win!!")
            gamerun = 0
            

    #ชนะแนวทะแยง        
        elif self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " ":
            self.display_board()
            print("Player " + self.board_array[1][1] + " Win!!")
            gamerun = 0
            
            
        elif self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " ":
            self.display_board()
            print("Player " + self.board_array[1][1] + " Win!!")
            gamerun = 0
            
            
        elif self.turn_count == 9:
            self.display_board()
            print("Draw")
            gamerun = 0

        
class Input_Processor(Board):
    def __init__(self):
        self.board_array = [['1','2','3'],['4', '5', '6'],['7', '8', '9']]
        self.player = "X"
        self.turn_count = 0 
    def input_checker(self):
        self.position =  input("Please input (1-9): ")
        return self.position

    
    def error_check(self):
        realInput = int(self.position) - 1
        if (realInput <= 8 and realInput >= 0):
            x = int(realInput%3)
            y = int(realInput//3)
            if self.board_array[y][x] != "X" and self.board_array[y][x] != "Y":
                self.board_array[y][x] = self.player
                return True
            else :
                print("Invalid Try Again")
                return False
            
            
board = Input_Processor()


while(not board.check_winner()):
    if gamerun == 1:
        board.display_board()
        #board.add_postion()
        board.input_checker()
        board.error_check()
        board.change_player()
    else:
        print("Game Over!")
        break
#6201012610079 วิชญ์สิฏฐ์ ใช้ศรีทอง
#6201012620040 คงเดช สมใจ 
#6201012620074 ณัฐชนน วะลับ 
#6201012620341 นางสาวตุลยา สารโพคา

##from xo_classText import start_game


class GameXO:
    def __init__(self):
        self.turn_count = 0
        self.board_array = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.player = "X"
        self.gamerun = 1
        
    def add_position(self,player,inputnum,board_array) :
        XPosition = inputnum % 3
        YPosition = inputnum // 3 
        board_array[XPosition,YPosition] = player 
        return board_array
        
    def check_winner(self,turn_count,gamerun):
        #global gamerun
        #global turn_count
        if self.board_array[0][0] == self.board_array[0][1] == self.board_array[0][2] != " ":
            print("ผู้เล่นฝ่าย " + self.board_array[6] + " ชนะ")
            gamerun = 0

        elif self.board_array[1][0] == self.board_array[1][1] == self.board_array[1][2] != " ":
            print("ผู้เล่นฝ่าย " + self.board_array[3] + " ชนะ")
            gamerun = 0

        elif self.board_array[2][0] == self.board_array[2][1] == self.board_array[2][2] != " ":
            print("ผู้เล่นฝ่าย " + self.board_array[0] + " ชนะ")
            gamerun = 0

    #ชนะแนวตั้ง 
        elif self.board_array[0][0] == self.board_array[1][0] == self.board_array[2][0] != " ":
            print("ผู้เล่นฝ่าย " + self.board_array[0] + " ชนะ")
            gamerun = 0

        elif self.board_array[0][1] == self.board_array[1][1] == self.board_array[2][1] != " " :
            print("ผู้เล่นฝ่าย " + self.board_array[1] + " ชนะ")
            gamerun = 0

        elif self.board_array[0][2] == self.board_array[1][2] == self.board_array[2][2] != " " :
            print("ผู้เล่นฝ่าย " + self.board_array[2] + " ชนะ")
            gamerun = 0

    #ชนะแนวทะแยง        
        elif self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " " :
            print("ผู้เล่นฝ่าย " + self.board_array[4] + " ชนะ")
            gamerun = 0

        elif self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " " :
            print("ผู้เล่นฝ่าย " + self.board_array[4] + " ชนะ")
            gamerun = 0

        elif turn_count == 9:
            print("เสมอ")
            
    def change_player(self,player) :
        if player == "O" :
            player = "X"
        elif player == "X":
            player = "O"
        return player

    def display_borad(self):
        print("-------")
        print("|"+self.board_array[0][0]+"|"+self.board_array[0][1]+"|"+self.board_array[0][2]+"|")
        print("-------")
        print("|"+self.board_array[1][0]+"|"+self.board_array[1][1]+"|"+self.board_arrayd[1][2]+"|")
        print("-------")
        print("|"+self.board_array[2][0]+"|"+self.board_array[2][1]+"|"+self.board_array[2][2]+"|")
        print("-------")

    def start_game(self ):
        while self.turn_count < 9 :
            if self.gamerun == 1 :
                self.display_borad()
                self.add_position()
                self.change_player()
                self.check_winner()     
            else:
                break
game = GameXO()
game.start_game()


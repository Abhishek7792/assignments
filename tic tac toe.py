#assignment 6
#tic tac toe game
import numpy        #package conataining array
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s="X"
p2s="O"    
          
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range (3):
            if board[r][c]== symbol:      #checking a match in rows for win
                count=count+1
            if count==3:
                print(symbol,"won")
                return True
    return False
def check_columns(symbol):
    for c in range(3):
        count=0
        for r in range (3):
            if board[r][c]==symbol:    # cheching match in column for win
                count=count+1 
            if count==3:
                print(symbol,"won")
                return True
    return False
def check_diagnols(symbol):             #checking diagnols
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,"won")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,"won")
        return True
    return False
    
def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagnols(symbol)    
def place(symbol):
    print(numpy.matrix(board))         #checking winner
    while(1):
        row=int(input("enter your row position 1 or 2 or 3 : "))
        column=int(input("enter column 1 or 2 or 3 : "))
        if row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]== "-" :
            break
        else:
            print("invalid input")              #user input 
    board[row-1][column-1]=symbol   
        
               
               
    
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")            #giving turn to both players
            place(p1s)
            if won(p1s):
                break
        else:
            print("O turn")      
            place(p2s)
            if won(p2s):
                break
        if not(won(p1s)) and not(won(p2s)):
            print("draw")
play()
    


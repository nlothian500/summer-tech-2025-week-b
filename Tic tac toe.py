board = [["-","-","-"], ["-","-","-"],["-","-","-"]]

player = "x"
runningame = True
while runningame == True:
    for b in range(3):
        for j in range(3):
            print(board[b][j],end="")
        print( )
    
    w = int(input("enter your row number"))
    f = int(input("enter your column number"))
    board[w][f] = player

    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        print(player + " won")
        runningame = False
        
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print(player + " won")
        runningame = False

    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        print(player + " won")
        runningame = False
        
    if board[2][1] == player and board[1][1] == player and board[0][1] == player:
        print(player + " won")
        runningame = False
    
    if board[2][0] == player and board[1][0] == player and board[0][0] == player:
        print(player + " won")
        runningame = False
    
    if board[2][2] == player and board[1][2] == player and board[0][2] == player:
        print(player + " won")
        runningame = False
        
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print(player + " won")
        runningame = False
        
    if board[2][2] == player and board[1][1] == player and board[0][0] == player:
        print(player + " won")
        runningame = False
    
    if player == "x":
        player = "o"
    elif player == "o":
        player = "x"
        


    
    
    
    
    
    
    
player == [0][0]
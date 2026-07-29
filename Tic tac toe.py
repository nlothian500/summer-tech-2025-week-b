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

    if player == [0][0] and player == [0][1] and player == [0][2]:
        print(player+"won")
        board == [0][0] and [0][1] and [0][2]
    if player == [1][0] and player == [1][1] and player == [1][2]:
        print(player+"won")
    if player == [2][0] and player == [2][1] and player == [2][2]:
        print(player+"won")

    if player == "x":
        player = "o"
    elif player == "o":
        player = "x"


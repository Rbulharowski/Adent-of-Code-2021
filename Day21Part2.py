player1turn = [[[5,0],[6,0]]]
player1track = [1]
player2turn = []
player2track = []
player1wins = 0
player2wins = 0
workspace = []
while len(player1turn) != 0 or len(player2turn) != 0:
    print(player1wins,player2wins)
    while len(player1turn) != 0:
        print("player1 turn")
        if [[player1turn[0][0][0]+3,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+3,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+3,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0])

        if [[player1turn[0][0][0]+4,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+4,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += 3 * player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+4,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0]*3)

        if [[player1turn[0][0][0]+5,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+5,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += 6 * player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+5,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0]*6)

        if [[player1turn[0][0][0]+6,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+6,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += 7 * player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+6,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0]*7)

        if [[player1turn[0][0][0]+7,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+7,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += 6 * player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+7,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0]*6)
            
        if [[player1turn[0][0][0]+8,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+8,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += 3 * player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+8,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0]*3)

        if [[player1turn[0][0][0]+9,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]] in player2turn:
            use = player2turn.index([[player1turn[0][0][0]+9,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track[use] += player1track[0]
        else:
            player2turn.append([[player1turn[0][0][0]+9,player1turn[0][0][1]],[player1turn[0][1][0],player1turn[0][1][1]]])
            player2track.append(player1track[0])

        print(len(player2turn), len(player1turn))
        player1turn.pop(0)
        player1track.pop(0)
    for i in range(len(player2turn)):
        if player2turn[i][0][0] > 10:
            player2turn[i][0][0] -= 10
        player2turn[i][0][1] += player2turn[i][0][0]
    print("Math")
    x = 0
    while x < len(player2turn):
        if player2turn[x][0][1] >= 21:
            player1wins += player2track[x]
            player2track.pop(x)
            player2turn.pop(x)
            x -= 1
        x += 1
        print(x,len(player2turn))
    while len(player2turn) != 0:
        print("player2 turn")
        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+3,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+3,player2turn[0][1][1]]])
            player1track[use] += player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+3,player2turn[0][1][1]]])
            player1track.append(player2track[0])

        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+4,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+4,player2turn[0][1][1]]])
            player1track[use] += 3 * player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+4,player2turn[0][1][1]]])
            player1track.append(player2track[0]*3)

        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+5,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+5,player2turn[0][1][1]]])
            player1track[use] += 6 * player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+5,player2turn[0][1][1]]])
            player1track.append(player2track[0]*6)

        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+6,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+6,player2turn[0][1][1]]])
            player1track[use] += 7 * player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+6,player2turn[0][1][1]]])
            player1track.append(player2track[0]*7)

        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+7,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+7,player2turn[0][1][1]]])
            player1track[use] += 6 * player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+7,player2turn[0][1][1]]])
            player1track.append(player2track[0]*6)

        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+8,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+8,player2turn[0][1][1]]])
            player1track[use] += 3 * player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+8,player2turn[0][1][1]]])
            player1track.append(player2track[0]*3)

        if [[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+9,player2turn[0][1][1]]] in player1turn:
            use = player1turn.index([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+9,player2turn[0][1][1]]])
            player1track[use] += player2track[0]
        else:
            player1turn.append([[player2turn[0][0][0],player2turn[0][0][1]],[player2turn[0][1][0]+9,player2turn[0][1][1]]])
            player1track.append(player2track[0])

        player2turn.pop(0)
        player2track.pop(0)
        print(len(player1turn), len(player2turn))
    for i in range(len(player1turn)):
        while player1turn[i][1][0] > 10:
            player1turn[i][1][0] -= 10
        player1turn[i][1][1] += player1turn[i][1][0]
    print("Math")
    x = 0
    while x < len(player1turn):
        if player1turn[x][1][1] >= 21:
            player2wins += player1track[x]
            player1track.pop(x)
            player1turn.pop(x)
            x -= 1
        x += 1
        print(x, len(player1turn))


print(player1wins, player2wins) 

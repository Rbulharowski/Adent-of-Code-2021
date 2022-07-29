octopi = [[1,1,7,2,7,2,8,8,7,4],
[6,7,5,1,4,5,4,2,8,1],
[2,6,1,2,3,4,3,5,3,3],
[1,8,8,4,8,7,7,5,1,1],
[7,5,7,4,3,4,6,2,4,7],
[2,1,1,7,4,1,3,7,4,5],
[7,7,6,6,7,3,6,5,1,7],
[4,3,3,1,7,8,3,4,4,4],
[4,8,4,1,2,1,5,8,2,8],
[6,8,5,7,7,6,6,2,7,3]]




while 17 == 16:
# #Used to edit the text file and create text file to make the bingo boards into an array
# with open('Flashstepdata.txt','r') as f:
#     contents = f.read()
#     changedtxt = contents.replace("", ",")
#     changedtxt = changedtxt.replace("\n", "],\n[")
#     changedtxt = changedtxt.replace("[,", "[")
#     changedtxt = changedtxt.replace(",]", "]")
# with open('editedflashstepdata.txt', 'w') as g:
#    g.writelines(changedtxt)
    print("\" Hello World \"")

flashes = 0

i = 0
y = 0
x = 0



while i < 100:
    y=0
    x=0
    while y < len(octopi):
        x=0
        while x < len(octopi[y]):
            octopi[y][x]+=1
            x+=1
            #print("add")
            #print(x,"x")
        y+=1
        #print(y,"y")
    #print(octopi)
    
    while 10 in octopi[0] or 10 in octopi[1] or 10 in octopi[2] or 10 in octopi[3] or 10 in octopi[4] or 10 in octopi[5] or 10 in octopi[6] or 10 in octopi[7] or 10 in octopi[8] or 10 in octopi[9]:
        #print("ten found")
        x=0
        y=0
        while y < len(octopi):
            x=0
            while x < len(octopi[y]):
                if octopi[y][x] == 10:
                    octopi[y][x] = 15
                    #print(flashes,i)
                    try:
                        if octopi[y+1][x] < 10:
                            octopi[y+1][x] +=1
                    except:
                        if 17 == 16:
                            print("Bot",y,x)
                    try:
                        if octopi[y+1][x-1] < 10 and x-1 > -1:
                            octopi[y+1][x-1] +=1
                    except:
                        if 17 == 16:
                            print("BotL",y,x)
                    try:
                        if octopi[y+1][x+1] < 10:
                            octopi[y+1][x+1] +=1
                    except:
                        if 17 == 16:
                            print("BotR",y,x)
                    try:
                        if octopi[y-1][x] < 10 and y-1 > -1:
                            octopi[y-1][x] +=1
                    except:
                        if 17 == 16:
                            print("Top",y,x)
                    try:
                        if octopi[y-1][x-1] < 10 and x-1 > -1 and y-1 > -1:
                            octopi[y-1][x-1] +=1
                    except:
                        if 17 == 16:
                            print("TopL",y,x)
                    try:
                        if octopi[y-1][x+1] < 10 and y-1 > -1:
                            octopi[y-1][x+1] +=1
                    except:
                        if 17 == 16:
                            print("TopR",y,x)
                    try:
                        if octopi[y][x+1] < 10:
                            octopi[y][x+1] +=1
                    except:
                        if 17 == 16:
                            print("Right",y,x)
                    try:
                        if octopi[y][x-1] < 10 and x-1 > -1:
                            octopi[y][x-1] +=1
                    except:
                        if 17 == 16:
                            print("Left",y,x)
                x+=1
            y+=1
    print(octopi)
    z = 0
    if 15 in octopi[0] or 15 in octopi[1] or 15 in octopi[2] or 15 in octopi[3] or 15 in octopi[4] or 15 in octopi[5] or 15 in octopi[6] or 15 in octopi[7] or 15 in octopi[8] or 15 in octopi[9]:
        y = 0
        while y < len(octopi):
            x=0
            while x < len(octopi[y]):
                if octopi[y][x] == 15:
                    octopi[y][x] = 0
                    flashes +=1
                    z += 1
                x+=1
            y+=1
    i += 1
    
    #print(z)
    print(i,flashes)


print(flashes)
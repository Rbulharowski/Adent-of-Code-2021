# Developed code with a lot of help from Eric Burden's explanation: https://www.ericburden.work/blog/2022/01/05/advent-of-code-2021-day-24/




# # while 17 == 16:
# #     # #Used to edit the text file and create text file to make the bingo boards into an array
# with open('arithmetic.txt','r') as f:
#   contents = f.read()
#   changedtxt = contents.replace("inp w\n", "[\"")
#   changedtxt = changedtxt.replace(" ", "\",\"")
#   changedtxt = changedtxt.replace("\n", "\"],\n[\"")
#   changedtxt = changedtxt.replace("],\n[\"[", "]],\n[[")
#   changedtxt = changedtxt.replace("\"],\n[\"", "\"],[\"")
# with open('editedarithmetic.txt', 'w') as g:
#    g.writelines(changedtxt)
# #     print("\" Hello World \"")




w = 0
x = 0
y = 0
z = 0
difference = 0

highestnumber = 0
modelnumber = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stacks = []
pairs = []
                        #               #                #                                                 #                 #               #               #               #               #               #                #              #                               #               #
instructions = [[["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","10"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","0"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","12"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","6"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","13"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","4"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","13"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","2"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","14"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","9"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-2"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","1"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","11"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","10"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-15"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","6"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-10"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","4"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","1"],["add","x","10"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","6"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-10"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","3"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-4"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","9"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-1"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","15"],["mul","y","x"],["add","z","y"]],
                [["mul","x","0"],["add","x","z"],["mod","x","26"],["div","z","26"],["add","x","-1"],["eql","x","w"],["eql","x","0"],["mul","y","0"],["add","y","25"],["mul","y","x"],["add","y","1"],["mul","z","y"],["mul","y","0"],["add","y","w"],["add","y","5"],["mul","y","x"],["add","z","y"]]]

#function built after the list of instructions, since the instructions are so consistent and repeat, you only have to read a few values from the list
def runinstructions(instructionline):
    global w, x, y, z, modelnumber,instructions,previousz
    previousz = z
    w = modelnumber[instructionline]
    x = 0
    x = (z%26) + int(instructions[instructionline][4][2])
    z = z // int(instructions[instructionline][3][2])
    if x == w:
        x = 0
    else:
        x = 1

    z = z * ((25*x)+1)
    z += ((w +int(instructions[instructionline][14][2]))*x)
    
def makenumber():
    blank = ""
    for h in modelnumber:
        blank += str(h)
    return int(blank)

def newnumber():
    global modelnumber
    last = len(modelnumber)-1

    while modelnumber[last] == 1:
        modelnumber[last] = 9
        last -= 1
    modelnumber[last] -= 1
    print(modelnumber)


for r in range(len(instructions)):
    stacks.append(r)
    if instructions[r][3][2] == "26":
        pairs.append([stacks[len(stacks)-2],stacks[len(stacks)-1]])
        for y in range(2):
            stacks.pop(len(stacks)-1)
        
for t in range(len(pairs)):
    difference = int(instructions[pairs[t][0]][14][2]) + int(instructions[pairs[t][1]][4][2])
    if difference < 0:
        modelnumber[pairs[t][0]] = 9
        modelnumber[pairs[t][1]] = 9 + difference
    else:
        modelnumber[pairs[t][0]] = 9 - difference
        modelnumber[pairs[t][1]] = 9
    
for g in range(len(instructions)):
    runinstructions(g)
    print(z)
if z == 0:
    highestnumber = makenumber()
else:
    "Big Issue"

print(highestnumber)


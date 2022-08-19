import time
pathing = [["by","TW"],
["start","TW"],
["fw","END"],
["QZ","END"],
["JH","by"],
["ka","start"],
["ka","by"],
["END","JH"],
["QZ","cv"],
["vg","TI"],
["by","fw"],
["QZ","by"],
["JH","ka"],
["JH","vg"],
["vg","fw"],
["TW","cv"],
["QZ","vg"],
["ka","TW"],
["ka","QZ"],
["JH","fw"],
["vg","hu"],
["cv","start"],
["by","cv"],
["ka","cv"]]




while 17 == 16:
# #Used to edit the text file and create text file to make the bingo boards into an array
# with open('mappingdata.txt','r') as f:
#     contents = f.read()
#     changedtxt = contents.replace("-", "\",\"")
#     changedtxt = changedtxt.replace("\n", "\"],\n[\"")
# with open('editedmappingdata.txt', 'w') as g:
#    g.writelines(changedtxt)
    print("\" Hello World \"")

routes = []
finishedroutes = []
workspace = []
directions = []

for i in range(len(pathing)):
    if "start" in pathing[i]:
        routes.append(["start"])
        if pathing[i][0] == "start":
            routes[len(routes)-1].append(pathing[i][1])
        else: 
            routes[len(routes)-1].append(pathing[i][0])

print(routes)

i = 0
newroutes = 0
while len(routes) != 0:
    workspace.append(routes[0])
    routes.pop(0)
    newroutes=0
    for x in range(len(pathing)):
        if workspace[0][len(workspace[0])-1] in pathing[x] and "start" not in pathing[x]:
            if pathing[x][0] == workspace[i][len(workspace[i])-1]:
                if pathing[x][1] not in workspace[0] and pathing[x][1].islower():
                    newroutes += 1
                    directions.append(pathing[x][1])
                elif pathing[x][1].isupper():
                    newroutes += 1
                    directions.append(pathing[x][1])
            else: 
                if pathing[x][0] not in workspace[0] and pathing[x][0].islower():
                    newroutes += 1
                    directions.append(pathing[x][0])
                elif pathing[x][0].isupper():
                    newroutes += 1
                    directions.append(pathing[x][0])
    #print(newroutes)
    if newroutes == 0:
        workspace.clear()
        print("deadend")
    else:
        bogus = []
        while len(workspace) != newroutes:
            bogus = workspace[0].copy()
            workspace.append(bogus)
        #print(workspace)
        #print(directions)
        if len(workspace) != len(directions):
            print("MASSIVE ERROR")
        newroutes = 0
        for x in range(len(workspace)):
            #print(x)
            #print(directions[x])
            workspace[x].append(directions[x])
            #print(workspace[x])
        print(workspace)
        while len(workspace) != 0:
            bogus = workspace[0].copy()
            if bogus[len(bogus)-1] == "END":
                finishedroutes.append(bogus)
            else:
                routes.append(bogus)
            workspace.pop(0)
        #print(routes)
        directions.clear()
        print(len(finishedroutes))

    
print(len(finishedroutes))     







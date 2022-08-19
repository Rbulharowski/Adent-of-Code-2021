import math
scanner0 = []
scanner0distance = [] 
scanner1 = []
scanner1distance = [] 
scanner2 = []
scanner2distance = [] 
scanner3 = []
scanner3distance = [] 
scanner4 = []
scanner4distance = [] 
scanner5 = []
scanner5distance = [] 
scanner6 = []
scanner6distance = [] 
scanner7 = []
scanner7distance = [] 
scanner8 = []
scanner8distance = [] 
scanner9 = []
scanner9distance = [] 
scanner10 = []
scanner10distance = [] 
scanner11 = []
scanner11distance = [] 
scanner12 = []
scanner12distance = [] 
scanner13 = []
scanner13distance = [] 
scanner14 = []
scanner14distance = [] 
scanner15 = []
scanner15distance = [] 
scanner16 = []
scanner16distance = [] 
scanner17 = []
scanner17distance = [] 
scanner18 = []
scanner18distance = [] 
scanner19 = []
scanner19distance = [] 
scanner20 = []
scanner20distance = [] 
scanner21 = []
scanner21distance = [] 
scanner22 = []
scanner22distance = [] 
scanner23 = []
scanner23distance = [] 
scanner24 = []
scanner24distance = [] 
scanner25 = []
scanner25distance = [] 
scanner26 = []
scanner26distance = [] 
scanner27 = []
scanner27distance = [] 


data = open("scanner.txt","r")
for k in data:
    if "scanner" in k:
        line = k.split(' ')
        #print(line[2])
        listname = "scanner"+line[2]
    if "," in k:
        changedtxt = k.replace("\n","")
        changedtxt = changedtxt.split(",")
        for l in range(len(changedtxt)):
            changedtxt[l] = int(changedtxt[l])
        eval(listname).append(changedtxt)

for j in range(28):
    listname = "scanner"+str(j)
    for l in range(len(eval(listname))):
        item = l + 1
        while item < len((eval(listname))):
            if l != len(eval(listname))-1:
                distance = math.sqrt(((eval(listname)[l][0] - eval(listname)[item][0])**2) + ((eval(listname)[l][1] - eval(listname)[item][1])**2) + ((eval(listname)[l][2] - eval(listname)[item][2])**2))
                eval(listname+"distance").append([l,item,round(distance,3)])
            item += 1

print(scanner0distance)


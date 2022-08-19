# # while 17 == 16:
#     # #Used to edit the text file and create text file to make the bingo boards into an array
with open('codedata.txt','r') as f:
    contents = f.read()
    changedtxt = contents.replace("", "\",\"")
with open('editedcodedata.txt', 'w') as g:
   g.writelines(changedtxt)
#     # print("\" Hello World \"")

adventinput = ["2","0","5","4","6","C","8","8","0","2","5","3","8","E","1","3","6","0","9","1","C","1","8","0","2","6","8","9","B","C","D","7","D","A","4","5","9","4","8","D","3","1","9","D","1","B","1","0","0","7","4","7","A","0","0","9","C","9","7","6","9","6","E","8","B","4","A","B","F","C","A","6","A","B","8","F","4","F","2","6","C","4","0","1","9","6","4","A","6","2","7","1","C","8","0","F","8","0","2","D","3","9","2","C","0","1","C","E","D","D","C","E","6","E","5","C","B","8","2","9","8","0","2","F","6","0","0","A","0","0","0","2","1","B","1","4","E","3","4","C","3","6","1","0","0","6","E","0","A","C","4","1","8","B","B","2","C","A","6","8","0","0","B","E","4","5","9","9","B","B","6","A","7","3","5","0","7","0","0","2","A","5","2","B","E","E","B","1","4","D","2","0","1","8","0","2","F","6","0","0","8","4","9","E","6","4","D","3","3","6","9","D","3","7","C","7","4","1","0","0","8","6","6","7","8","5","B","3","D","0","A","D","F","D","8","E","6","0","1","E","5","E","B","9","D","E","2","3","6","6","D","9","3","E","C","B","8","B","0","4","0","1","4","2","C","B","8","A","C","E","0","7","C","C","B","5","C","F","3","4","C","A","8","9","3","8","0","4","1","0","B","6","1","3","4","C","E","6","F","E","F","1","0","4","A","2","B","2","0","0","2","4","3","3","9","6","9","7","6","A","0","0","4","0","1","A","4","5","0","0","4","3","1","3","D","6","8","4","3","5","D","B","D","D","D","A","6","1","C","E","6","4","2","8","C","0","1","4","9","1","A","E","B","F","0","C","7","E","5","8","0","A","E","0","0","C","C","C","4","0","1","B","8","6","5","1","4","2","1","6","8","8","0","3","7","0","E","E","3","4","4","3","D","2","0","1","3","D","F","0","0","3","7","5","0","0","0","4","3","6","1","3","4","3","D","8","8","8","0","0","0","8","4","C","4","C","8","B","1","1","6","A","6","7","9","0","1","8","3","0","0","7","4","0","0","1","0","C","8","5","7","1","B","A","3","2","0","8","0","3","5","0","D","A","0","D","4","2","8","0","0","0","4","3","A","3","0","4","4","1","8","9","A","E","0","1","7","4","B","3","1","4","D","7","6","E","1","F","3","A","C","F","3","B","D","A","E","3","E","E","7","2","9","8","F","F","1","3","4","0","0","2","E","F","9","D","B","C","D","0","6","4","4","1","2","7","E","3","C","A","E","7","F","C","B","A","9","A","8","0","3","9","3","5","4","4","F","9","A","9","2","7","C","9","7","3","D","F","1","A","5","0","0","9","6","5","A","5","C","E","A","9","4","C","4","D","D","A","5","6","5","8","B","9","4","C","6","C","3","0","0","2","A","7","9","8","A","6","2","9","C","F","2","1","2","8","0","5","3","2","B","A","B","4","F","4","C","7","2","7","1","E","4","5","E","E","6","E","7","1","D","8","1","4","3","A","9","B","C","7","9","4","8","8","0","4","A","B","9","4","D","1","D","6","0","0","6","A","C","2","0","0","E","C","1","E","8","A","1","0","C","0","0","0","1","0","9","8","5","3","1","6","A","3","5","C","3","6","2","0","0","6","1","E","6","4","1","6","4","4","D","6","6","1","A","4","C","0","1","2","9","9","3","E","9","9","2","0","8","F","C","6","0","0","9","7","8","0","2","F","2","8","F","5","2","8","F","7","3","8","6","0","6","0","0","8","C","A","4","7","2","0","5","4","0","0","8","1","4","C","8","9","C","C","8","8","9","0","0","6","4","D","4","0","0","A","B","4","B","E","0","A","6","6","F","2","B","F","2","5","3","E","7","3","A","E","8","4","0","1","4","2","4","A","7","B","F","B","1","6","C","0","0","3","7","E","0","6","C","E","0","6","4","1","E","0","0","1","3","B","0","8","0","1","0","A","8","9","3","0","C","E","2","B","9","8","0","3","5","1","1","6","1","D","C","3","7","3","0","0","6","6","2","7","4","1","8","8","B","0","2","0","0","5","4","A","5","E","1","6","9","6","5","9","4","0","0","5","7","8","9","5","A","D","E","B","5","B","F","5","6","A","6","3","5","A","D","E","2","3","5","4","1","9","1","D","7","0","5","6","6","2","7","3","A","6","F","5","B","0","7","8","2","6","6","0","0","8","D","8","0","2","2","2","0","0","D","4","6","E","8","2","9","1","C","4","4","0","1","A","8","C","F","0","C","E","3","3","C","E","D","E","5","5","E","9","F","9","8","0","2","B","A","0","0","B","4","B","D","4","4","A","5","E","A","2","D","1","0","C","C","0","0","B","4","0","3","1","6","8","0","0","B","A","E","1","0","0","3","5","8","0","A","6","D","6","0","2","6","F","0","0","0","9","0","E","5","0","0","2","4","0","0","7","C","9","5","0","0","2","5","8","0","6","8","8","5","0","0","3","5","C","0","0","A","4","0","1","2","E","D","8","0","4","0","B","4","0","0","D","7","1","0","0","2","A","F","5","0","0","2","8","4","0","0","9","7","0","0","2","2","6","3","3","6","C","A","4","9","8","0","4","7","1","D","6","5","5","E","2","5","D","4","6","5","0","8","8","8","0","2","3","A","B","0","0","5","2","5","C","A","E","5","C","B","A","5","E","4","2","8","6","0","0","B","E","0","0","3","9","9","3","7","7","8","C","B","4","7","3","2","9","9","6","E","9","8","8","7","A","E","3","F","3","1","1","C","2","9","1","0","0","4","B","D","3","7","5","1","7","C","0","0","4","1","E","7","8","0","A","7","8","0","8","8","0","2","A","F","8","C","1","C","0","0","D","0","C","D","B","E","4","A","C","A","D","6","9","B","3","B","0","0","4","E","1","3","B","D","F","2","3","C","A","E","7","3","6","8","C","9","F","6","2","4","4","8","F","6","4","5","4","6","0","0","8","E","0","0","3","4","F","3","7","2","0","1","9","2","A","6","7","A","D","9","2","5","4","9","1","7","4","5","4","2","0","0","D","C","E","8","0","1","C","9","9","A","D","F","1","8","2","5","7","5","B","B","A","A","C","A","C","7","F","8","5","8","0"]


convertedbinary = []
orderkeeper = []
version = []
typeID = []
Checker = True
neededlength = 0
digcounter = 0
packcounter = 0
# lengthtracker = []
# subtracker = []
packetorder = []
lengthadded = 0

def hexatobinary(num1,num2,num3,num4):
  convertedbinary.append(num1)
  convertedbinary.append(num2)
  convertedbinary.append(num3)
  convertedbinary.append(num4)
def popper(num):
  for x in range(num):
    convertedbinary.pop(0)
def numberbuilder(num):
  safe = ""
  #print(num)
  i = 0
  while i < num:
    safe += str(convertedbinary[i])
    i += 1
  #print(safe)
  binary = int(safe,2)
  return binary

def fournumberbuilder(num):
  safe = ""
  #print(num)
  for i in range(num):
    if i%5 != 0:
      safe += str(convertedbinary[i])
  #print(safe)
  binary = int(safe,2)
  return binary

  
def operatoradder():
  global orderkeeper, typeID, packetorder
  if typeID[len(typeID)-1] == 0:
    orderkeeper.append(["+", len(packetorder)])
  elif typeID[len(typeID)-1] == 1:
    orderkeeper.append(["*", len(packetorder)])
  elif typeID[len(typeID)-1] == 2:
    orderkeeper.append(["min", len(packetorder)])
  elif typeID[len(typeID)-1] == 3:
    orderkeeper.append(["max", len(packetorder)])
  elif typeID[len(typeID)-1] == 5:
    orderkeeper.append([">", len(packetorder)])
  elif typeID[len(typeID)-1] == 6:
    orderkeeper.append(["<", len(packetorder)])
  elif typeID[len(typeID)-1] == 7:
    orderkeeper.append(["=", len(packetorder)])
  else:
    print("Issue")
    
for x in range(len(adventinput)):
  if adventinput[x] == "0":
    hexatobinary(0,0,0,0)
  elif adventinput[x] == "1":
    hexatobinary(0,0,0,1)
  elif adventinput[x] == "2":
    hexatobinary(0,0,1,0)
  elif adventinput[x] == "3":
    hexatobinary(0,0,1,1)
  elif adventinput[x] == "4":
    hexatobinary(0,1,0,0)
  elif adventinput[x] == "5":
    hexatobinary(0,1,0,1)
  elif adventinput[x] == "6":
    hexatobinary(0,1,1,0)
  elif adventinput[x] == "7":
    hexatobinary(0,1,1,1)
  elif adventinput[x] == "8":
    hexatobinary(1,0,0,0)
  elif adventinput[x] == "9":
    hexatobinary(1,0,0,1)
  elif adventinput[x] == "A":
    hexatobinary(1,0,1,0)
  elif adventinput[x] == "B":
    hexatobinary(1,0,1,1)
  elif adventinput[x] == "C":
    hexatobinary(1,1,0,0)
  elif adventinput[x] == "D":
    hexatobinary(1,1,0,1)
  elif adventinput[x] == "E":
    hexatobinary(1,1,1,0)
  elif adventinput[x] == "F":
    hexatobinary(1,1,1,1)

def clearworkspace():
  global workspace, orderkeeper, x, level
  #print(workspace)
  level = orderkeeper[workspace[0]-1][1]
  while len(workspace) != 0:
    orderkeeper.pop(workspace[len(workspace)-1])
    workspace.pop(len(workspace)-1)
  x= -1
  # print(orderkeeper)
  # print("")
  # print("")
  

#print(convertedbinary)

#print(len(convertedbinary))


while Checker == True:
  digcounter = 0
  packcounter = 0
  lengthadded = 0
  try:
    if str(convertedbinary[3])+ str(convertedbinary[4]) + str(convertedbinary[5]) == "100" and len(convertedbinary) > 10 and 1 in convertedbinary:
      #print("Made it to 4")
      version.append(int(str(convertedbinary[0])+ str(convertedbinary[1]) + str(convertedbinary[2]),2))
      popper(3)
      typeID.append(int(str(convertedbinary[0])+ str(convertedbinary[1]) + str(convertedbinary[2]),2))
      popper(3)
      digcounter += 6
      while convertedbinary[digcounter-6] != 0:
        digcounter += 5
        #print("Remove")
      digcounter += 5
      #print(digcounter,"4")
      orderkeeper.append([fournumberbuilder(digcounter-6),len(packetorder)])
      popper(digcounter-6)
      packcounter += 1
      #print("stopping")
    elif str(convertedbinary[3])+ str(convertedbinary[4]) + str(convertedbinary[5]) != "100" and 1 in convertedbinary:
      #print("Made it to other")
      version.append(int(str(convertedbinary[0])+ str(convertedbinary[1]) + str(convertedbinary[2]),2))
      popper(3)
      typeID.append(int(str(convertedbinary[0])+ str(convertedbinary[1]) + str(convertedbinary[2]),2))
      popper(3)
      operatoradder()
      digcounter += 6
      if convertedbinary[0] == 0:
        digcounter += 1
        popper(1)
        packetorder.append([numberbuilder(15),0,"Len"])
        digcounter += 15
        popper(15)
        lengthadded = 1
      else:
        digcounter += 1
        popper(1)
        packetorder.append([numberbuilder(11),0,"Num"])
        digcounter += 11
        popper(11)
        packcounter -= 1
      packcounter += 1
      #print(digcounter, "other")
    else:
      Checker = False

    if len(packetorder) != 0:
      if lengthadded == 0:
        for x in range(len(packetorder)):
          if packetorder[x][2] == "Len":
            packetorder[x][1] += digcounter
      else: 
        for x in range(len(packetorder)-1):
          if packetorder[x][2] == "Len":
            packetorder[x][1] += digcounter
   
      if packcounter == 1 and packetorder[len(packetorder)-1][2] == "Num":
        packetorder[len(packetorder)-1][1] += 1
      elif packcounter == 0 and packetorder[len(packetorder)-2][2] == "Num":
        packetorder[len(packetorder)-2][1] += 1
      elif packcounter == 1 and lengthadded != 0 and packetorder[len(packetorder)-2][2] == "Num":
        packetorder[len(packetorder)-2][1]+= 1

      while packetorder[len(packetorder)-1][0] == packetorder[len(packetorder)-1][1]:
        packetorder.pop(len(packetorder)-1)
      
  except:
    Checker = False
  print(packetorder, digcounter,packcounter)
total = 0
for i in range(len(version)):
  total += version[i]
#print(total)
#print(version, typeID, orderkeeper)
print(orderkeeper)
# print(lengthtracker)
# print(subtracker)

workspace = []
level = 0
while len(orderkeeper) != 1:
  x = 0
  level = 0
  while x < len(orderkeeper):
    if isinstance(orderkeeper[x][0], int) and orderkeeper[x][1] == level:
      workspace.append(x)
    elif isinstance(orderkeeper[x][0], str) and orderkeeper[x][1] == level:
      level += 1
      workspace.clear()
    if (orderkeeper[x][1] < level or x == len(orderkeeper)-1) and len(workspace) != 0:
      #print("Inside")
      if orderkeeper[workspace[0]-1][0] == "+":
        total = 0
        for y in workspace:
          total += orderkeeper[y][0]
        orderkeeper[workspace[0]-1][0] = total
        clearworkspace()
      elif orderkeeper[workspace[0]-1][0] == "*":
        total = orderkeeper[workspace[0]][0]
        j = 1
        while j < len(workspace):
          total *= orderkeeper[workspace[j]][0]
          j += 1
        orderkeeper[workspace[0]-1][0] = total
        clearworkspace()
      elif orderkeeper[workspace[0]-1][0] == "min":
        total = orderkeeper[workspace[0]][0]
        for y in workspace:
          if orderkeeper[y][0] < total:
            total = orderkeeper[y][0]
        orderkeeper[workspace[0]-1][0] = total
        clearworkspace()
      elif orderkeeper[workspace[0]-1][0] == "max":
        total = orderkeeper[workspace[0]][0]
        for y in workspace:
          if orderkeeper[y][0] > total:
            total = orderkeeper[y][0]
        orderkeeper[workspace[0]-1][0] = total
        clearworkspace()
      elif orderkeeper[workspace[0]-1][0] == ">":
        if len(workspace) == 2:
          if orderkeeper[workspace[0]][0] > orderkeeper[workspace[1]][0]:
            orderkeeper[workspace[0]-1][0] = 1
          else:
            orderkeeper[workspace[0]-1][0] = 0
        else:
          print("Miscalculation, greater")
          # print(orderkeeper)
          # print(workspace)
        clearworkspace()
      elif orderkeeper[workspace[0]-1][0] == "<":
        if len(workspace) == 2:
          if orderkeeper[workspace[0]][0] < orderkeeper[workspace[1]][0]:
            orderkeeper[workspace[0]-1][0] = 1
          else:
            orderkeeper[workspace[0]-1][0] = 0
        else:
          print("Miscalculation, lesser")
        clearworkspace()
      elif orderkeeper[workspace[0]-1][0] == "=":
        if len(workspace) == 2:
          if orderkeeper[workspace[0]][0] == orderkeeper[workspace[1]][0]:
            orderkeeper[workspace[0]-1][0] = 1
          else:
            orderkeeper[workspace[0]-1][0] = 0
        else:
          print("Miscalculation, equal")
        clearworkspace()
      #print("end",x)
    x += 1
print(orderkeeper)
      
      
      

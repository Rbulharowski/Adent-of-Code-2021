# while 17 == 16:
#     # #Used to edit the text file and create text file to make the bingo boards into an array
with open('lights.txt','r') as f:
  contents = f.read()
  changedtxt = contents.replace("", ",")
  changedtxt = changedtxt.replace(".", "0")
  changedtxt = changedtxt.replace("#", "1")
  changedtxt = changedtxt.replace(",\n", "],\n[")
  changedtxt = changedtxt.replace("[,", "[")
with open('editedlights.txt', 'w') as g:
   g.writelines(changedtxt)
#     print("\" Hello World \"")

lights = [[0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,1,0,1],
[0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0],
[1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0],
[0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1],
[0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,1],
[0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1],
[0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0],
[0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1],
[1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0],
[1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0],
[0,0,0,1,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1],
[1,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
[1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,1],
[0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0],
[1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0],
[0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0],
[0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1],
[1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0],
[1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
[0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1],
[0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0],
[0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0],
[1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0],
[0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0],
[1,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1],
[1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0],
[1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1],
[0,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0],
[0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1],
[1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
[1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
[1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1],
[0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,1],
[1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1],
[1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0],
[1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0],
[0,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1],
[0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0],
[1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1],
[1,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1],
[1,0,1,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,0],
[0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,1],
[0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0],
[1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0],
[1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,0,0],
[1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1],
[1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1],
[0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0],
[1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1],
[0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0],
[1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0],
[0,1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1],
[1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,1,1],
[1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1],
[0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0],
[1,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1],
[0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0],
[0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0],
[1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0],
[1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1],
[0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0],
[0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1],
[0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1],
[1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1],
[0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1],
[1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0],
[1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1],
[1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0],
[1,1,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1],
[0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1],
[1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1],
[0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0],
[0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1],
[1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0],
[0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1],
[0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1],
[0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1],
[1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1],
[1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0],
[1,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1],
[1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1],
[1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1],
[0,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0],
[1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1],
[1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1],
[0,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0],
[0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1],
[0,1,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0],
[1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1],
[0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1],
[1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1]]
enhanced = []
algorithm = [1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0]

line = []
binary = ""
empty = []
for y in range(len(lights)):
  for x in range(55):
    lights[y].insert(0,0)
    lights[y].append(0)
print(len(lights[0]))

for y in range(len(lights[0])):
  empty.append(0)

for y in range(55):
  lights.insert(0,empty.copy())
  lights.append(empty.copy())

void = str(0)

for i in range(50):
  print("enhanced " + str(i+1) + " times")
  for y in range(len(lights)):
    line = []
    
    for x in range(len(lights[y])):
      binary = ""
      if y == 0:
        binary+= void + void + void
        if x == 0:
          binary += void + str(lights[y][x]) + str(lights[y][x+1]) + void + str(lights[y+1][x]) + str(lights[y+1][x+1])
        elif x == len(lights[y])-1:
          binary += str(lights[y][x-1]) + str(lights[y][x]) + void + str(lights[y+1][x-1]) + str(lights[y+1][x]) + void
        else: 
          binary += str(lights[y][x-1]) + str(lights[y][x]) + str(lights[y][x+1]) + str(lights[y+1][x-1]) + str(lights[y+1][x]) + str(lights[y+1][x+1])
      elif y == len(lights)-1:
        if x == 0:
          binary += void + str(lights[y-1][x]) + str(lights[y-1][x+1]) + void + str(lights[y][x]) + str(lights[y][x+1])
        elif x == len(lights[y])-1:
          binary += str(lights[y-1][x-1]) + str(lights[y-1][x]) + void + str(lights[y][x-1]) + str(lights[y][x]) + void
        else: 
          binary += str(lights[y-1][x-1]) + str(lights[y-1][x]) + str(lights[y-1][x+1]) + str(lights[y][x-1]) + str(lights[y][x]) + str(lights[y][x+1])
        binary+= void + void + void
      else:
        if x == 0:
          binary += void + str(lights[y-1][x]) + str(lights[y-1][x+1]) + void + str(lights[y][x]) + str(lights[y][x+1]) + void + str(lights[y+1][x]) + str(lights[y+1][x+1])
        elif x == len(lights[y])-1:
          binary += str(lights[y-1][x-1]) + str(lights[y-1][x]) + void + str(lights[y][x-1]) + str(lights[y][x]) + void + str(lights[y+1][x-1]) + str(lights[y+1][x]) + void
        else:
          binary += str(lights[y-1][x-1]) + str(lights[y-1][x]) + str(lights[y-1][x+1]) + str(lights[y][x-1]) + str(lights[y][x]) + str(lights[y][x+1]) + str(lights[y+1][x-1]) + str(lights[y+1][x]) + str(lights[y+1][x+1])
      #print(binary)
      line.append(algorithm[int(binary,2)])
    enhanced.append(line.copy())
  lights = enhanced.copy()
  #print(lights)
  enhanced.clear()
  print(void)
  if void == "1" and 1 in lights[0]:
    print("Not wide enough")
  void = str(algorithm[int(str(void)+str(void)+str(void)+str(void)+str(void)+str(void)+str(void)+str(void)+str(void),2)])

total = 0
for y in range(len(lights)):
  for x in range(len(lights[y])):
    if lights[y][x] == 1:
      total += 1

print(total)
        

while 17 == 16:
    # #Used to edit the text file and create text file to make the bingo boards into an array
    # with open('basepolymer.txt','r') as f:
    #     contents = f.read()
    #     changedtxt = contents.replace("", "\",\"")
    #     changedtxt = changedtxt.replace("\n", "]")
    # with open('editedbasepolymer.txt', 'w') as g:
    #    g.writelines(changedtxt)
    print("\" Hello World \"")

while 17 == 16:
    # #Used to edit the text file and create text file to make the bingo boards into an array
    # with open('polymerdata.txt','r') as f:
    #     contents = f.read()
    #     changedtxt = contents.replace(" -> ", "\",\"")
    #     changedtxt = changedtxt.replace("\n", "\"],\n[\"")
    # with open('editedpolymerdata.txt', 'w') as g:
    #    g.writelines(changedtxt)
    print("\" Hello World \"")

polymer = [
    "C", "N", "B", "P", "H", "F", "B", "O", "P", "C", "S", "P", "K", "O", "F",
    "N", "H", "V", "K", "V"
]
chemistry = [["CS", "S"], ["FB", "F"], ["VK", "V"], ["HO", "F"], ["SO", "K"],
             ["FK", "B"], ["VS", "C"], ["PS", "H"], ["HH", "P"], ["KH", "V"],
             ["PV", "V"], ["CB", "N"], ["BB", "N"], ["HB", "B"], ["HV", "O"],
             ["NC", "H"], ["NF", "B"], ["HP", "B"], ["HK", "S"], ["SF", "O"],
             ["ON", "K"], ["VN", "V"], ["SB", "H"], ["SK", "H"], ["VH", "N"],
             ["KN", "C"], ["CC", "N"], ["BF", "H"], ["SN", "N"], ["KP", "B"],
             ["FO", "N"], ["KO", "V"], ["BP", "O"], ["OK", "F"], ["HC", "B"],
             ["NH", "O"], ["SP", "O"], ["OO", "S"], ["VC", "O"], ["PC", "F"],
             ["VB", "O"], ["FF", "S"], ["BS", "F"], ["KS", "F"], ["OV", "P"],
             ["NB", "O"], ["CF", "F"], ["SS", "V"], ["KV", "K"], ["FP", "F"],
             ["KC", "C"], ["PF", "C"], ["OS", "C"], ["PN", "B"], ["OP", "C"],
             ["FN", "F"], ["OF", "C"], ["NP", "C"], ["CK", "N"], ["BN", "K"],
             ["BO", "K"], ["OH", "S"], ["BH", "O"], ["SH", "N"], ["CH", "K"],
             ["PO", "V"], ["CN", "N"], ["BV", "F"], ["FV", "B"], ["VP", "V"],
             ["FS", "O"], ["NV", "P"], ["PH", "C"], ["HN", "P"], ["VV", "C"],
             ["NK", "K"], ["CO", "N"], ["NS", "P"], ["VO", "P"], ["CP", "V"],
             ["OC", "S"], ["PK", "V"], ["NN", "F"], ["SC", "P"], ["BK", "F"],
             ["BC", "P"], ["FH", "B"], ["OB", "O"], ["FC", "N"], ["PB", "N"],
             ["VF", "N"], ["PP", "S"], ["HS", "O"], ["HF", "N"], ["KK", "C"],
             ["KB", "N"], ["SV", "N"], ["KF", "K"], ["CV", "N"], ["NO", "P"]]

mixingpot = []

temp = ""
i = 0
elements = ["B","C","F","H","K","N","O","P","S","V"]
occurance = [0,0,0,0,0,0,0,0,0,0]
mixingpot.append(polymer[0])
for y in range(10):
  i = 0
  while i < len(polymer)-1:
    temp = polymer[i]+polymer[i+1]
    for x in range(len(chemistry)):
      if temp in chemistry[x][0]:
        # print(polymer[i], polymer[i+1], chemistry[x])
        mixingpot.append(chemistry[x][1])
        mixingpot.append(polymer[i+1])
    i += 1
  if (len(mixingpot)-len(polymer)) != len(polymer)-1:
    print("Fail to the tenth degree", len(polymer)-1, (len(mixingpot)-len(polymer)))
  polymer = mixingpot.copy()
  mixingpot.clear()
  mixingpot.append(polymer[0])
  print(y)
  print(len(polymer))

for x in range(len(elements)):
  for u in range(len(polymer)):
    if elements[x] in polymer[u]:
      occurance[x] += 1

print(len(polymer))
occurance.sort()
print(occurance)
print(occurance[len(occurance)-1]-occurance[0])

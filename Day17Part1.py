import math

finalheight = 0


x1 = 57
x2 = 116
y1 = -148
y2 = -198
xlowvelocity = 0
xhighvelocity = 0
testpositions = []
positionx = 0
positiony = 0


def quadratic_up (num):
  global xlowvelocity
  lowervalue = ((math.sqrt((8 * num)+1))-1)/2
  xlowvelocity = math.ceil(lowervalue)
def quadratic_down (num):
  global xhighvelocity
  highervalue = ((math.sqrt((8 * num)+1))-1)/2
  xhighvelocity = math.floor(highervalue)


quadratic_up(x1)
quadratic_down(x2)
print(xlowvelocity,xhighvelocity)
xstorage = xlowvelocity
ystorage = 1
testpositions = []
xposition = 0
yposition = 0
while xstorage <= xhighvelocity:
  ystorage = 1
  print(xstorage,"#####")
  while ystorage < abs(y2):
    testpositions = []
    testx = xstorage
    testy = ystorage
    xposition = 0
    yposition = 0
    point = 0
    while point != -1:
      testpositions.append([xposition,yposition])
      xposition += testx
      yposition += testy
      if testx != 0:
        testx -= 1
      testy -= 1
      if testpositions[len(testpositions)-1][1] < y2:
        point = -1
      elif testpositions[len(testpositions)-1][0] >= x1 and testpositions[len(testpositions)-1][1] <= y1 and testpositions[len(testpositions)-1][1] >= y2:
        for x in range(len(testpositions)):
          if testpositions[x][1] > finalheight:
            finalheight = testpositions[x][1]
        point = -1
    ystorage += 1
  xstorage += 1
      
print(finalheight)
      

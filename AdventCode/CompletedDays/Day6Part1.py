lanternpop = [3,5,1,5,3,2,1,3,4,2,5,1,3,3,2,5,1,3,1,5,5,1,1,1,2,4,1,4,5,2,1,2,4,3,1,2,3,4,3,4,4,5,1,1,1,1,5,5,3,4,4,4,5,3,4,1,4,3,3,2,1,1,3,3,3,2,1,3,5,2,3,4,2,5,4,5,4,4,2,2,3,3,3,3,5,4,2,3,1,2,1,1,2,2,5,1,1,4,1,5,3,2,1,4,1,5,1,4,5,2,1,1,1,4,5,4,2,4,5,4,2,4,4,1,1,2,2,1,1,2,3,3,2,5,2,1,1,2,1,1,1,3,2,3,1,5,4,5,3,3,2,1,1,1,3,5,1,1,4,4,5,4,3,3,3,3,2,4,5,2,1,1,1,4,2,4,2,2,5,5,5,4,1,1,5,1,5,2,1,3,3,2,5,2,1,2,4,3,3,1,5,4,1,1,1,4,2,5,5,4,4,3,4,3,1,5,5,2,5,4,2,3,4,1,1,4,4,3,4,1,3,4,1,1,4,3,2,2,5,3,1,4,4,4,1,3,4,3,1,5,3,3,5,5,4,4,1,2,4,2,2,3,1,1,4,5,3,1,1,1,1,3,5,4,1,1,2,1,1,2,1,2,3,1,1,3,2,2,5,5,1,5,5,1,4,4,3,5,4,4]
weeks = [0,0,0,0,0,0,0]
births = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
daytracker = 0
fishtracker = 0
totaldaytracker = 0
#print(len(lanternpop))
# while daytracker <= 256:
#     #print("hello")
#     fishtracker = 0
#     while fishtracker < len(lanternpop):
#         #print("Vietnam")
#         if lanternpop[fishtracker] != 0:
#             lanternpop[fishtracker] -= 1
#         elif lanternpop[fishtracker] == 0:
#             lanternpop[fishtracker] = 6
#             lanternpop.append(9)
#         fishtracker += 1
#     #print(str(len(lanternpop)) + "//" + str(daytracker))
#     daytracker += 1

while fishtracker < len(lanternpop):
    weeks[lanternpop[fishtracker]] += 1
    fishtracker += 1

fishtracker = 300
for i in range(256):
    daytracker = i%14
    print(weeks)
    weeks[daytracker%7] += births[daytracker]
    fishtracker += weeks[daytracker%7]
    births[(daytracker+9)%14] += weeks[daytracker%7]
    births[daytracker] = 0
    print(births)

    
print(fishtracker)
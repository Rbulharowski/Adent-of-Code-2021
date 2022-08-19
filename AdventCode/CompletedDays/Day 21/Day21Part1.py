class Player :
  def __init__(self,startposition):
    self.position = startposition
    self.score = 0

def your_turn(player):
  global player1, player2, die_rolls, die_number, turnmovement
  turnmovement = 0
  for i in range(3):
    if (die_number+1)%100 == 0:
      die_number = 100
    else:
      die_number = (die_number+1)%100
    turnmovement += die_number
  die_rolls += 3
  player.position = (player.position + turnmovement)%10
  if player.position == 0:
    player.position = 10
  player.score += player.position
  
player1 = Player(5)
player2 = Player(6)

print(player1.position)
print(player2.position)

die_rolls = 0
die_number = 0
turnmovement = 0

while player1.score < 1000 and player2.score < 1000:
  if player1.score < 1000 and player2.score < 1000:
    your_turn(player1)
  if player1.score < 1000 and player2.score < 1000:
    your_turn(player2)
  print(player1.score,player2.score)

if player1.score < player2.score:
  print(player1.score*die_rolls)
else:
  print(player2.score*die_rolls)

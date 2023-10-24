#DEFINE A PLAYER

class player:
  def play(self):
    print("The Player is playing cricket.")
class batsman(player):
  def play(self):
    print("The batsman is batting.")
class bowler(player): 
  def play(self):
    print("The bowler is bowler.")
Batsman=batsman()
Bowler=bowler()
Batsman.play()
Bowler.play()
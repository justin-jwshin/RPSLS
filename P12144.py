from RPSLS_player import RPSLS_player

class P12144(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    return "paper"
    
        
  
  def update(self, result: str, competitor_shot: str):
    if self.update[1]== "rock":
        self.shoot= "scissors"
    elif self.update[1]== "scissors":
        self.shoot= "rock"
    elif self.update[1]== "paper":
        self.shoot= "spock"
    elif self.update[1]== "lizard":
        self.shoot= "scissors"
    elif self.update[1]== "spock":
        self.shoot= "paper"
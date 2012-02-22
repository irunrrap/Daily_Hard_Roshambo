import random

class player():
    
    def __init__(self):
        self.wins = 0
        self.moves = {1: "Paper", 2: "Scissors", 3: "Rock"}
        self.current_move = ""
        return(None)
    
    def perform_move(self):
        self.current_move = self.moves[random.randint(1,3)]
        return(self.current_move)

    def register_win(self):
        self.wins+=1
        return(None)

def win_test(value1, value2):
    if (((value1, value2) == ("Paper", "Rock")) or
        ((value1, value2) == ("Scissors", "Paper")) or
        ((value1, value2) == ("Rock", "Scissors"))):
        return(1)
    else:
        return(None)

p1, p2 = player(), player()

rounds_played, rounds_to_play = 0, 1000

while rounds_played < rounds_to_play:
    rounds_played+=1
    p1.perform_move()
    p2.perform_move()
    if p1.current_move == p2.current_move:
        pass
    else:
        if win_test(p1.current_move, p2.current_move):
            p1.register_win()
        else:
            p2.register_win()
        

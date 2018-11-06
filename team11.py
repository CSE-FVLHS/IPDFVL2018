team_name = 'Wesley'
strategy_name = 'Error or Beat'
strategy_description = '---ERROR---'

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
       return 'b'
    elif their_history[-1].upper() == 'B':
        return 7302002
    else:
        return 'b'
        
      
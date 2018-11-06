from __future__ import print_function

team_name = 'RipShellShock'
strategy_name = 'Collude 70% unless betrayed within last 5 rounds.'
strategy_description = '''\
Betray if ever betrayed.
If I haven't been betrayed yet, I'll betray starting with the th round.
'''

import random

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[1] and their_history[1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history) == 0:
        return 'c'

    elif 'b' in their_history[-5:]: # If the other player has betrayed within last 5 rounds, 
        return 'b'               # Betray.
    else:
        if random.random()<0.15: # 15% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 85% of the time collude
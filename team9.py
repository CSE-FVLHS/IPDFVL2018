####
# Each team's file must define four tokens:
#     team_name: Win?
#     strategy_name: random first turn then decide
#     move: A function that returns 'c' or 'b'
####

team_name = 'Test team' # Only 10 chars displayed.
strategy_name = 'random 1st turn then respond to their history'
strategy_description = 'it looks at history'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''

    import random
    if len(my_history) == 0:
        return random.choice ('cb')
    elif (their_score) < my_score:
        if (my_score) > 0:
            return 'b'
        else:
            if len(their_history) == 'ccc' :
                return random.choice ('cb')
            elif len(their_history) == 'bbb':
                    return 'b'
            elif len(their_history) == 'cbcb':
                return 'b'
            else:
                return 'c'
    else:
        return 'b'
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Win' # Only 10 chars displayed.
strategy_name = 'Winners'
strategy_description = 'Winning?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    '''
    import random
    if len(their_history) == 0:
        return 'b'
    elif len(their_history) == 1:
        return 'b'
    elif their_history[-2:] == 'bc':
        return 'c'
    elif their_history[-2:] == 'cb':
        return 'b'
    elif their_history[-2:] == 'bb':
        return 'b'
    elif their_history[-2:] == 'cc':
        return 'b'
    else:
        return 'b'
        
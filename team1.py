####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Test team #2' # Only 10 chars displayed.
strategy_name = 'Random than counter most '
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    import random 
    
    if len(my_history)==0:
       return random.choice('cbcb')
    if their_history.count('c')>their_history.count('b'):
       return 'b'
    else:
        return 'c'
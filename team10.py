####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Flounder' # Only 10 chars displayed.
strategy_name = 'Aiming for top 5'
strategy_description = 'Will usually return b, unless certain requirements are fulfilled. If a user is returning something other than c or b with some intent of trickery, the program will return whatever they are returning. '
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if their_history.count('c') or ('C') > their_history.count('b')*3 or ('B')*3:
        return 'b'
    elif their_history.count('bcb') or ('BCB'):
        return 'b'
    elif their_history.count('c')*3 < their_history.count('b'):
        return 'b'
    elif 'c' in their_history or len(their_history)>25:
        return 'bc'
    else:
        if their_history[-1] != 'c' or 'b':
            return their_history[-1]
        else:
            return 'b'
            
       
        
            
    
        
        
        
    
    
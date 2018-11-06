####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Thunder Taco Cat'
strategy_name = 'complient until provoked'
strategy_description = 'play c until betrayed'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
        return 'c'
    if len(my_history) >= 1:
        if their_history[-1] == 'c':
            if len(my_history) >= 2:
                if their_history[-2] == 'c':
                    if len(my_history) >= 3:
                        if their_history[-3] == 'c':
                            return 'c'
                    else:
                        return 'b'
                    return 'c'
                else:
                    return 'b'
            else:
                return 'b'
            return 'c'
        else:
            return 'b'
    else:
        return 'b'
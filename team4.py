####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Best of da Best'
strategy_name = 'Gradual'
strategy_description = 'Do not betray unless betrayed. If betrayed, use betray for the number of times Ive betrayed'
    
def move(my_history, their_history, my_score, their_score):
    repeat = 1
    turns = 1
    if len(their_history)-turns == 'b' and turns <= repeat:
        turns += 1
        return 'b'
    elif turns > repeat:
        turns = 1
        repeat += 1
    elif len(their_history-1) == 'c':
        return 'c'
    else:
        return 'b'

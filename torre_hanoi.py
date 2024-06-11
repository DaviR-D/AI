import copy

def is_valid_state(state):
    for stack in state:
        if(not stack == sorted(stack, reverse=True)):
            return False
    return True

def generate_next_states(state, visited_states):
    valid_states = []
    for stack in range(3):
        for stack2 in range(-1, -3, -1):
            if(len(state[ stack + stack2]) > 0):
                new_state = copy.deepcopy(state)
                new_state[stack].append(new_state[ stack + stack2].pop())
                if(is_valid_state(new_state)):        
                    if(new_state not in visited_states):
                        print(new_state)                      
                       

initial_state = [[5,4,3,2,1], [], []]

final_state = [[], [], [5,4,3,2,1]]

visited_states = []

generate_next_states(initial_state, visited_states)
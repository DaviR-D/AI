def is_valid_state(stack):
    if(not stack == sorted(stack, reverse=True)):
        return False
    return True

def generate_next_states(state, visited_states):
    valid_states = []
    for stack in range(3):
        for stack2 in range(-1, -3, -1):
            print(state[stack], state[stack + stack2])
            if(len(state[ stack + stack2]) > 0):
                potential_stack = state[stack] + [state[ stack + stack2][-1]]
                if(is_valid_state(potential_stack)):
                    new_state = state
                    new_state[stack].append(new_state[ stack + stack2].pop())
                    if(new_state not in visited_states):
                        #print(new_state)
                        pass
                       

initial_state = [[5,4,3,2], [1], []]

final_state = [[], [], [5,4,3,2,1]]

visited_states = [[[5,4,3,2,1], [], []]]

generate_next_states(initial_state, visited_states)
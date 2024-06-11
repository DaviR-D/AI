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
                        valid_states.append(new_state)
    return valid_states                     

def bfs(initial_state, final_state):
    visited_states = []
    queue = [initial_state]
    #predecessors = {tuple(map(tuple, initial_state)): None}

    while queue:
        state = queue.pop(0)
        visited_states.append(state)
        print(state)
        if state == final_state:
        #     path = []
        #     while state is not None:
        #         path.append(state)
        #         state = predecessors[tuple(map(tuple, state))]
        #     path.reverse()
        #     for step in path:
        #         print(step)
            return
        for next_state in generate_next_states(state, visited_states):
            if(next_state not in visited_states):
                queue.append(next_state)
                #predecessors[tuple(map(tuple, next_state))] = state


def dfs(initial_state, final_state):
    visited_states = []
    stack = [initial_state]

    while stack:
        state = stack.pop()
        visited_states.append(state)
        print(state)
        if(state == final_state):
            return
        for next_state in generate_next_states(state, visited_states):
            if next_state not in visited_states:
                visited_states.append(next_state)
                stack.append(next_state)
            



initial_state = [[5,4,3,2,1], [], []]

final_state = [[], [], [5,4,3,2,1]]

dfs(initial_state, final_state)
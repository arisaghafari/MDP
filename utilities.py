import enum


class Actions(enum.Enum):
    N = 1
    W = 2
    S = 3
    E = 4
    EXIT = 5


def initialize_world_parameters(world_type):
    if world_type == 'smallWorld':
        return (3, 3), {(0, 2): 1, (1, 2): -1}
    if world_type == 'largeWorld':
        return (10, 10), {(0, 9): 1, (1, 9): -1}
    else:
        raise Exception("Wrong Entry.")


def initialize_mdp_parameters(width, height, exit_locations):
    v_states = [[0 for i in range(0, width)] for j in range(height)]  # Current step's V*(s) grid.
    pre_v_states = [[0 for i in range(0, width)] for j in range(height)]  # Last step's V*(s) grid.
    policy = [[Actions.N for i in range(0, width)] for j in range(height)]  # Current step's policy gird.
    for exit_state, exit_reward in exit_locations.items():
        exit_x, exit_y = exit_state
        v_states[exit_x][exit_y] = exit_reward
        pre_v_states[exit_x][exit_y] = exit_reward
        policy[exit_x][exit_y] = Actions.EXIT
    return v_states, pre_v_states, policy

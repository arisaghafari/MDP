from utilities import Actions, initialize_mdp_parameters
import sys

class MDPProblem:
    """

    :param grid_dim: a tuple of (height, width) which declares dimensions of the world grid.
    :param exit_locations: a dictionary with exit states as keys and rewards as values.
    example given: self.exit_locations[(0, 2)] = -1 or self.exit_locations = {(0, 2): -1, ...}


    """
    #hamkari ba shafagh rastegari va yazdane seyedi
    def __init__(self, grid_dim, exit_locations):
        self.grid_dim = grid_dim
        self.exit_locations = exit_locations

    def compute_policy(self, reward=-0.01, gama=1, steps=10):
        """

        :param reward: reward of moving from one cell to another. (Living reward)
        :param gama: Discount coefficient
        :param steps: depth of computation. (How many turns agent can play)
        :return:
        1-2D grid of computed V*_k(s) after each step.
        Example Given for 3x3 world after some steps.
       [ 0     0.8  1
       -0.02 -0.1 -1
        0   -0.02  0 ]
        2- A 2D grid of computed Policies. (same as v_states but filled with Actions class instances.)
        a naive policy:
      [ Actions.N Actions.N Actions.EXIT
        Actions.N Actions.N Actions.EXIT
        Actions.N Actions.N Actions.N ]
        """

        width, height = self.grid_dim

        # Use pre_v_states for keeping previous V states. (former iteration)
        v_states, pre_v_states, policy = initialize_mdp_parameters(width, height, self.exit_locations)
        for row in v_states:
            print(*row)
        print('******************')
        for row in pre_v_states:
            print(*row)
        print('******************')
        for row in policy:
            print(*row)
        print('******************')
        maximum = -9999
        actions = [Actions.N, Actions.S, Actions.E, Actions.W]
        for k in range(0, steps):
            for i in range(0, width):
                for j in range(0, height):
                    if v_states[i][j] == 1 or v_states[i][j] == -1:
                        continue
                    qlist = []
                    for action in actions:
                        transactions = self.get_transition((i,j) , action)
                        q = 0
                       # print("list transaction : ", transactions)
                        for transaction in transactions:
                            q += transaction[2] * (reward + gama * pre_v_states[transaction[0]][transaction[1]]) 
                        qlist.append(q)
                    Qmax = max(qlist)   
                    v_states[i][j] = Qmax
                    policy[i][j] = actions[qlist.index(Qmax)]
            pre_v_states = v_states
            # DO NOT CHANGE yield Line. You should return V and Pi computed in each step.
            yield v_states, policy

    def get_transition(self, state, action):
        """

        :param state: a tuple of (x, y) as dimensions
        :param action: object of Actions enum class. (such as:
        Actions.N)
        :return: given current state and chosen action, returns next non-determinist states with
        corresponding transition probabilities. example given: [(x, y, 0.8), (z, t, 0,2), ...] means after choosing
        action, agent goes to (x, y) with probability of 80% and goes to (z, t) with probability of 20%.

        """

        next_state_dict = {Actions.N: (-1, 0), Actions.S: (1, 0), Actions.E: (0, 1), Actions.W: (0, -1)}
        non_determinist_dict = {Actions.N: Actions.E, Actions.E: Actions.S, Actions.S: Actions.W, Actions.W: Actions.N}
        transitions = []
        next_x, next_y = tuple(map(sum, zip(next_state_dict[action], state)))
        if (0 <= next_x < self.grid_dim[0]) and (0 <= next_y < self.grid_dim[1]):
            transitions += [(next_x, next_y, 0.8)]
        next_x, next_y = tuple(map(sum, zip(next_state_dict[non_determinist_dict[action]], state)))
        if (0 <= next_x < self.grid_dim[0]) and (0 <= next_y < self.grid_dim[1]):
            transitions += [(next_x, next_y, 0.2)]
        return transitions

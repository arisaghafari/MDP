import sys

from mdp_problems import MDPProblem
from utilities import initialize_world_parameters
from visualize import run_mdp


# DO NOT CHANGE THIS FILE
world_type = sys.argv[1].split('=')[1]

grid_dim, exit_locations = initialize_world_parameters(world_type)
mdp_problem = MDPProblem(grid_dim=grid_dim, exit_locations=exit_locations)

run_mdp(mdp_problem.compute_policy(), grid_dim)

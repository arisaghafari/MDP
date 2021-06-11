import tkinter as tk
from utilities import initialize_world_parameters, Actions
import time

# DO NOT CHANGE THIS FILE
actions_dict = {Actions.N: 'North', Actions.S: 'South',
                Actions.E: 'East', Actions.W: 'West', Actions.EXIT: 'EXIT'}


def create_grid(event=None):
    w = c.winfo_width()  # Get current width of canvas
    h = c.winfo_height()  # Get current height of canvas
    c.delete('grid_line')  # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, int(600 / dw)):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, int(600 / dh)):
        c.create_line([(0, i), (w, i)], tag='grid_line')


root = tk.Tk()

c = tk.Canvas(root, height=600, width=600, bg='white')


def run_mdp(v_stars_generator, world_dims, steps=10):
    globals()['dw'] = world_dims[0]
    globals()['dh'] = world_dims[1]
    for k, (v_states, policy) in enumerate(v_stars_generator):
        v_states = [[round(v_states[y][x], 3) for x in range(0, dh)] for y in range(dw)]
        for i, row in enumerate(v_states):
            for j, v in enumerate(row):
                time.sleep(1 / (dw * dw))
                c.create_text((600 / dh) * (j + .5),
                              (600 / dw) * (i + .5),
                              text=v, fill='blue', tag='v')
                c.create_text((600 / dh) * (j + .5),
                              (600 / dw) * (i + .5) - 150 / dh,
                              text=actions_dict[policy[i][j]], tag='p')

            c.pack(fill=tk.BOTH, expand=True)
            c.bind('<Configure>', create_grid)
            c.update()
        if k < steps - 1:
            c.delete('p')
            c.delete('v')

    root.mainloop()

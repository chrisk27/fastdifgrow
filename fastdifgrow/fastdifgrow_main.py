"""
This script runs the basic simulations for the Differential Growth Turing Pattern Formation.
It is the same process that is described in the original Differential Growth Paper.

To change parameters, edit the corresponding functions.

Currently, will run each simulation for 10**9 Monte Carlo steps.
"""

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from initialize import initcond, neighbors


def sim_parameters():
    """This function defines the initial parameters used in simulations"""
    global rows, cols, h, per_cycle, num_cycles
    rows = 100
    cols = 100
    h = 15
    per_cycle = 10**7
    num_cycles = 10**2


def reaction_rates():
    """This function defines the reaction rates for each process"""
    global bx, bm, dx, dm, sm, sx, lx
    bx = 1  # birth of xantophores
    bm = 0  # birth of melanophores

    dx = 0  # death of xantophores
    dm = 0  # death of melanophores

    sm = 1  # short-range killing of xantophore by melanophore
    sx = 1  # short-range killing of melanophore by xantophore
    lx = 2.5  # long-range activation/birth strength
    return 



def sim_setup(row=100, col=100):
    """This function sets up the initial simulations, calling initial conditions and neighbors"""
    array, irid = initcond.basic(row, col)
    up, down, left, right = neighbors.calc4neighbors(row, col)
    return array, irid, up, down, left, right


def run_sim(array, irid, up, down, left, right, h=15, num_loops=10**2, per_loop=10**7):
    """This function runs the simulations and outputs the final matrix"""
    total = bx + bm + dx + dm + sm + sx + lx
    P_bx = bx/total
    P_bm = bm/total
    P_dx = dx/total
    P_dm = dm/total
    P_sm = sm/total
    P_sx = sx/total
    P_lx = lx/total 
    for loop in range(num_loops):
        idx0 = np.random.randint(low=0, high=rows, size=per_loop, dtype=np.uint8)
        idx1 = np.random.randint(low=0, high=cols, size=per_loop, dtype=np.uint8)
        process = np.random.rand(per_loop)

        for n in range(per_loop):
            pn = process[n]
            location = (idx0[n], idx1[n])
            well = array[location]
            if pn < P_lx:
                if (well == 0) & (~ irid[location]):
                    angle = random.random() * 2 * math.pi
                    cosangle = math.cos(angle)
                    sinangle = math.sin(angle)
                    i_new = np.around(location[0] + cosangle * h, decimals=0) % array.shape[0]
                    j_new = np.around(location[1] + sinangle * h, decimals=0) % array.shape[1]
                    if array[int(i_new), int(j_new)] == 1:
                        array[location] = 2  # has melanophore form distance away
            
            elif pn < P_lx + P_sx:
                if (well == 2):
                    neigh = ['u', 'd', 'l', 'r']
                    choice = random.choice(neigh)

                    if choice == 'u':  # chooses neighboring value
                        neigh_val = array[up[location], location[1]]
                    elif choice == 'd':
                        neigh_val = array[down[location], location[1]]
                    elif choice == 'l':
                        neigh_val = array[location[0], left[location]]
                    else:
                        neigh_val = array[location[0], right[location]]
                    
                    if neigh_val == 1:
                        array[location] = 0  # kills melanophore

            elif pn < P_lx + P_sx + P_sm:
                if (well == 1):
                    neigh = ['u', 'd', 'l', 'r']
                    choice = random.choice(neigh)

                    if choice == 'u':  # chooses neighboring value
                        neigh_val = array[up[location], location[1]]
                    elif choice == 'd':
                        neigh_val = array[down[location], location[1]]
                    elif choice == 'l':
                        neigh_val = array[location[0], left[location]]
                    else:
                        neigh_val = array[location[0], right[location]]
                    
                    if neigh_val == 2:
                        array[location] = 0  # kills xantophore

            elif pn < P_lx + P_sx + P_sm + P_bx:
                if well == 0:
                    array[location] = 1  # births xantophore

            elif pn < P_lx + P_sx + P_sm + P_bx + P_bm:
                if well == 0:
                    array[location] = 2  # births melanophore
                
            elif pn < P_lx + P_sx + P_sm + P_bx + P_bm + P_dx:
                if well == 1:
                    array[location] = 0  # kills xantophore

            elif pn < P_lx + P_sx + P_sm + P_bx + P_bm + P_dx + P_dm:
                if well == 2:
                    array[location] = 0  # kills melanophore

    return array


def plotter(array):
    """This function plots the arrays in a similar manner to the original paper:
    Yellow pixels are xantophores
    Black pixels are melanophores
    White pixels are empty
    """
    img = np.empty((array.shape[0], array.shape[1], 3), dtype=np.float32)
    img[array == 0, :] = [1, 1, 1]  # sets empty cells to white
    img[array == 2, :] = [0, 0, 0]  # sets melanophores to black
    img[array == 1, :] = [1, 1, 0]  # sets xantophores to yellow
    return img


if __name__ == '__main__':
    startTime = datetime.now()
    sim_parameters()
    reaction_rates()
    array, irid, up, down, left, right = sim_setup(rows, cols)
    final = run_sim(array, irid, up, down, left, right)
    image = plotter(final)
    print(datetime.now()-startTime)
    plt.imshow(image)
    plt.show()

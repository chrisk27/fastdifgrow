"""
This module contains functions that will create various initial states for the differential growth simulations.

Each function will require inputs for the size of the array (row and col).
In addition, some will have variable inputs for creating the iridophore prepattern.

Each function will output the initial state and the iridophore array, even if it's empty.
"""

import numpy as np


#  A note on the arrays:
#  Each experimental (initial) array is an ndarray filled with uint8s.
#  In this array, 0 indicates an empty array, 1 indicates a xantophore, and 2 indicates a melanophore.
#  The iridophore array is a boolean ndarray, where True indicates that there is an iridophore there.

def basic(row, col):
    """Generates an initial state with all empty cells"""
    output = np.zeros((row, col), dtype = np.uint8)
    irid = np.zeros((row, col), dtype = bool)
    return output, irid


def iridophore_band(row, col, bandwidth=1):
    """Generates an initial empty state, except for an initial band of iridophores which pre-patterns the system"""
    output = np.zeros((row, col), dtype = np.uint8)
    irid = np.zeros((row, col), dtype = bool)
    irid[0:bandwidth, :] = True  # Assigns iridophores to a row
    irid = np.roll(irid, floor((row - bandwidth) / 2), axis=0)  # rotates array so iridophores are in the middle
    return output, irid


def random_start(row, col, irid_ratio=0):
    """Generates a random starting state, and a random distribution of iridophores at proportion = irid_ratio"""
    output = np.zeros((row, col), dtype = np.uint8)
    rand_array = np.random.rand(row, col)
    output[rand_array < 1/3] = 1  # randomly assigns xantophores
    output[rand_array > 2/3] = 2  # randomly assigns melanophores

    irid_rand = np.random.rand(row, col) < irid_ratio

    return output, irid_rand
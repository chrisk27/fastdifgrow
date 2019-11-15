"""
This module calculates a new array for each of the desired neighbors. This is done by adding or subtracting the indices from
each other, so that the location in this array is filled with a value that corresponds to the neighboring well's index.

Each function takes in a rows and columns argument, and forms the array from there.

The output of each function is the matrix that corresponds to the right type of neighbor.
"""

import numpy as np


def row_up1_array(row, col):

"""
This module calculates a new array for each of the desired neighbors. This is done by adding or subtracting the indices from
each other, so that the location in this array is filled with a value that corresponds to the neighboring well's index.

Each function takes in a rows and columns argument, and forms the array from there.

The output of each function is the matrix that corresponds to the right type of neighbor.
"""

import numpy as np
import pandas as pd  # For visualizing in interactive console


def row_up1_array(row, col):
    """This function establishes an array that contains the index for the row above each entry"""
    up1_array = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        up1_array[i, :] = np.ones(col, dtype = np.uint8) * ((i - 1) % row)
    return up1_array


def row_down1_array(row, col):
    """This function establishes an array that contains the index for the row below each entry"""
    down1_array = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        down1_array[i, :] = np.ones(col, dtype = np.uint8) * ((i + 1) % row)
    return down1_array


def col_left1_array(row, col):
    """This function establishes an array that contains the index for the column left of each entry"""
    left1_array = np.zeros((row, col), dtype=np.uint8)
    for j in range(col):
        left1_array[:, j] = np.ones(row, dtype = np.uint8) * ((j - 1) % col)
    return left1_array

def col_right1_array(row, col):
    """This function establishes an array that contains the index for the column left of each entry"""
    right1_array = np.zeros((row, col), dtype=np.uint8)
    for j in range(col):
        right1_array[:, j] = np.ones(row, dtype = np.uint8) * ((j + 1) % col)
    return right1_array


def calc4neighbors(row, col):
    """This function calculates all 4 of the neighbor arrays, so it's easier to write into main code"""
    up1 = row_up1_array(row, col)
    down1 = row_down1_array(row, col)
    left1 = col_left1_array(row, col)
    right1 = col_right1_array(row, col)
    return up1, down1, left1, right1

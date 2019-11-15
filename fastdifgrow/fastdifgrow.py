"""
This script runs the basic simulations for the Differential Growth Turing Pattern Formation.
It is the same process that is described in the original Differential Growth Paper.

To change parameters, edit the corresponding functions.

Currently, will run each simulation for 10**9 Monte Carlo steps.
"""

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


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


def sim_setup():
    """This function sets up the initial simulations, calling initial conditions, probabilities, and neighbors"""
    return "Will write later"
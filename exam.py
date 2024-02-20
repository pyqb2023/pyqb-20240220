# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: February 20, 2024
#
# You can solve the exercises below by using standard Python 3.11 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.11/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC](https://docs.pymc.io).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2324/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question)**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```
#

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az   # type: ignore

# ### Exercise 1 (max 2 points)
#
# The file [dogs.csv](./dogs.csv) (Jarkoff Hugo, Lorre Guillaume, & Humbert Eric. (2023). Dog Health Vitals Dataset [Data set]. Zenodo. https://doi.org/10.5281/zenodo.8020390) is a collection of recordings and vital statistics related to the health of dogs. It includes data captured during various recording sessions, providing insights into the physiological characteristics of the dogs.
#
#     - duration: Duration of the recording session (in seconds).
#     - pet_id: Unique identifier for each dog.
#     - breeds: Main breed of the dog.
#     - weight: Weight of the dog at the time of measurement (in kg).
#     - age: Age of the dog at the time of measurement (in years).
#     - ecg_pulses: Array of floats separated by commas, each representing the timestamp (in seconds from the beginning of the signal) of an identified heart pulse on the recorded ECG signal.
#
# Load the data in a Pandas dataframe using the first column as the index.

pass

# ### Exercise 2 (max 3 points)
#
# Check (i.e., write an assertion) that each recording referring to a specific dog (identified by its `pet_id`) has exactlt the same `breeds`,`weight`,`age`.
#

pass

# ### Exercise 3 (max 4 points)
#
# Consider the dog with `pet_id` $= 22$: make a scatter plot of the first 15 `ecg_pulse`s values for all its ecg recordings (30 in total). Use different Y values and colors for each line of the scatter points, such that all the lines are in the same plot but they do not overlap and are easier to compare.
#

pass

# ### Exercise 4 (max 7 points)
#
# Define a function `deltas` that takes a list of sorted (increasingly) float values and a total duration and returns a list of deltas between the values. The first delta is always equal to the first value of the list and the last delta is difference between the total duration (greater than all the values) and the last values. For example, if the list of values is `[0.98, 2.51, 2.82, 3.39]` and the total duration is 4, the result is `[0.98, 1.53, 0.31, 0.57, .61]`.
#
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

pass


# +
# You can test your docstrings by executing this cell

import doctest
doctest.testmod()
# -

# ### Exercise 5 (max 4 points)
#
# Add a column `mean_ecg_delta` to the data with the average values of the deltas of the `ecg_pulses` as computed by the function defined in Exercise 4 (by using the `duration` of the recordings). When there is no `ecg_pulse` recording (`NaN`), the value `mean_ecg_delta` should be `NaN`.  
#

pass

# ### Exercise 6 (max 4 points)
#
# Plot together (with different colors) the deltas for the `ecg_pulse` recording of dog with `pet_id` $= 32$, the X axis should be the interval (0, `duration`).
#

pass

# ### Exercise 7 (max 5 points)
#
# Make a dataframe `obs` with one row for each `pet_id` and its `breeds`, `weight`, `age`, and the maximal `mean_ecg_delta`.
#

pass

# ### Exercise 8 (max 4 points)
#
# Consider this statistical model and the observations collected in `obs` (see previous exercise):
#
# - a parameter $\alpha$ is normally distributed with $\mu = 0$ and $\sigma = 1$ 
# - a parameter $\beta$ is normally distributed with $\mu = 1$ and $\sigma = 1$ 
# - a parameter $\gamma$ is exponentially distributed with $\lambda = 1$
# - the observed `mean_ecg_delta` is normally distributed with standard deviation $\gamma$ and a mean given by $\alpha + \beta \cdot W$ (where $W$ is the correspondig value of `weight`).
#
# Code this model with pymc, sample the model, and plot the summary of the resulting estimation by using `az.plot_posterior`. 
#

pass


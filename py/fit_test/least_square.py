"""
the following will calculate least square regression for each subject data at
site 1 (upper back)
objective: determine wheter or not this regression is the best fit for (n=15) subject's data

steps.
1. get data from each subject and condition
2. divide data in trial and test
3.
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
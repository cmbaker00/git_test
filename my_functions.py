import numpy as np


def logistic_growth(r = 1, k = 10, IC = 1, ts = 0, tf = 10, tstep = 0.1):
    t = np.arange(ts, tf + tstep, tstep)
    N = np.zeros(len(t))
    for i in range(len(t)):
        if i == 0:
            N[i] = IC
        else:
            N[i] = 
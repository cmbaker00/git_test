import numpy as np
import matplotlib.pyplot as plt

def logistic_growth(r = 1, k = 10, IC = 1, ts = 0, tf = 10, tstep = 0.1):
    t = np.arange(ts, tf + tstep, tstep)
    N = np.zeros(len(t))
    for i in range(len(t)):
        if i == 0:
            N[i] = IC
        else:
            dndt = N[i-1]*r*(1-N[i-1]/k)*tstep
            N[i] = N[i-1] + dndt
    return t, N

t, n = logistic_growth()
plt.plot(t,n)
plt.show()
# experimenting with logistic map and bifurcation diagram

import numpy as np
import matplotlib.pyplot as plt


# logistic map
def lfunc(x, r):
    return r * x * (1 - x)

# mandelbrot
def mfunc(x, c):
    return x*x + c


x_init = 0.00001    # parameter...
N = 1000            # systems to consider over possible r values
iterations = 1500   # run logistic function this many times for each r in each system
keep_last = 100     # throw away all but the last iterations

r_min = 3.55
r_max = 3.64

func = lfunc

    
r_vals = np.linspace(r_min, r_max, N)
x_vals = np.ones(N) * x_init
i_start = iterations - keep_last

for i in range(iterations):
    x_vals = func(x_vals, r_vals)
    if i >= i_start:
        plt.plot(r_vals, x_vals, ",k")


plt.xlabel("r")
plt.ylabel("x")
plt.show()

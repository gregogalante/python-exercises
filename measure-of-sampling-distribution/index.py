import numpy as np
import pandas as pd
import scipy.stats as stats
import pylab as p

np.random.seed(1234)
long_breaks = stats.poisson.rvs(loc=10, mu=60, size=3000)
short_breaks = stats.poisson.rvs(loc=10, mu=15, size=6000)
breaks = np.concatenate((long_breaks, short_breaks))
mean = breaks.mean()

point_estimates = []

for x in range(500):
    sample = np.random.choice(a = breaks, size = 100)
    point_estimates.append(sample.mean())

pd.DataFrame(point_estimates).hist()
p.show()

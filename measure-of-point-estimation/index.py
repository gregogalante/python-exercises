import numpy as np
import pandas as pd
import scipy.stats as stats

# A point estimate is an estimate of a population parameter based on
# sample data.

# Working with employes answers for question:
# "how many minutes on an average do you take braks for?"

# Method used to initialize RandomState
np.random.seed(1234)

# Represents 3000 people who take about 60 minute break -> 3000 answers to the question that will be on the longer side.
long_breaks = stats.poisson.rvs(loc = 10, mu = 60, size = 3000)

# Represents 6000 people who take about 15 minute break -> 6000 answers to the question that will be on the shorter side.
short_breaks = stats.poisson.rvs(loc = 10, mu = 15, size = 6000)

# Represents the final breaks
breaks = np.concatenate((long_breaks, short_breaks))

# Find total mean
mean = breaks.mean()
print 'The total breaks mean is', mean

# Take a random group of 9000 employes
sample_breaks = np.random.choice(a = breaks, size = 100)

# Calculate the point estimate
point_estimate = sample_breaks.mean()

difference_mean = mean - point_estimate
print 'The difference between real mean and the point estimate is', difference_mean

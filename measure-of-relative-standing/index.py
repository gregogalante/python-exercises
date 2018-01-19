import numpy as np
import matplotlib.pyplot as plt
import pylab as p

people_friends = [1100, 800, 250, 1900, 1453, 200, 39, 789, 1200, 456, 349, 222, 1093]

z_scores = []

m = np.mean(people_friends) # mean
s = np.std(people_friends) # standard deviation

print 'the mean for people_friends is:', m
print 'the standard deviation for people_friends is:', s

for people_friend in people_friends:
    z = (people_friend - m) / s
    z_scores.append(z)

print 'the list of relative standings for people_friends is:', z_scores

y_pos = range(len(people_friends))
plt.bar(y_pos, z_scores)

p.show()

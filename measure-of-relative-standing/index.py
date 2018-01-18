import numpy as np

people_friends = [1100, 800, 250, 1900, 1453, 200, 39, 789, 1200, 456, 349, 222, 1093]

# ugly version:

z_scores = []

m = np.mean(people_friends) # mean
s = np.std(people_friends) # standard deviation

print 'the mean for people_friends is:', m
print 'the standard deviation for people_friends is:', s

for people_friend in people_friends:
    z = (people_friend - m) / s
    z_scores.append(z)

print 'the list of relative standings for people_friends is:', z_scores

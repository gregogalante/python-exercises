import random
import matplotlib.pyplot as plt
import pylab as p

def random_variable_of_dice_roll():
    return random.randint(1, 7)

avgs = []
num_trials = range(100, 10000, 10)
for num_trial in num_trials:
    trials = []
    for trial in range(1, num_trial):
        trials.append(random_variable_of_dice_roll())
    avgs.append(sum(trials) / float(num_trial))

plt.plot(num_trials, avgs)
plt.xlabel('Number of trials')
plt.ylabel('Average')

p.show()

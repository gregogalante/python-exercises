import numpy

results = [1, 1, 2, 4, 2, 3, 5, 5, 3, 1, 2, 4, 5, 1, 2, 2, 1, 5, 4, 4, 3, 3, 3, 5]

num_items = len(results)
product = 1
for result in results:
    product *= result

geometric_mean = product**(1./num_items)

print 'the geometric mean is:', geometric_mean
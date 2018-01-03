import numpy

results = [1, 1, 2, 4, 2, 3, 5, 5, 3, 1, 2, 4, 5, 1, 2, 2, 1, 5, 4, 4, 3, 3, 3, 5]

sorted_results = sorted(results)

print sorted_results

mean = numpy.mean(results)

print 'the mean is:', mean

median = numpy.median(results)

print 'the median is:', median

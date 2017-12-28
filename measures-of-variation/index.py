import numpy

results = [1, 1, 2, 4, 2, 3, 5, 5, 3, 1, 2, 4, 5, 1, 2, 2, 1, 5, 4, 4, 3, 3, 3, 5]

# Calculate the standard variation:
# 1. find the mean of the data
# 2. for each number of the dataset, substract it from the mean and than square it
# 3. find the average of each square difference
# 4. take the square root of the number obtained in step three

mean = numpy.mean(results)
squared_differences = []
for result in results:
    difference = result - mean
    squared_difference = difference**2
    squared_differences.append(squared_difference)

average_squared_difference = numpy.mean(squared_differences)
standard_variation = numpy.sqrt(average_squared_difference)

print 'the mean is:', mean
print 'the standard variation is:', standard_variation

import numpy

# Define a series of user likes (range 1-5) for films by [commedies, romantic, action] values
user = numpy.array([5, 1, 3])
# Define a series of movie typologies (range 1-5) by [commedies, romantic, action] values
movie1 = numpy.array([4, 5, 1])
movie2 = numpy.array([5, 1, 5])

# Get the dot product for movies
dot_product_1 = numpy.dot(user, movie1)
dot_product_2 = numpy.dot(user, movie2)

print 'the dot product for movie 1 is:', dot_product_1 # -> 28
print 'the dot product for movie 2 is:', dot_product_2 # -> 41 # The movie 2 is better to movie 1 for the user
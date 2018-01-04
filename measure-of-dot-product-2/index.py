import numpy

# Define a series of user likes (range 1-5) for films by [commedies, romantic, action] values
user = numpy.array([5, 1, 3])

# Define a random matrix of 10 000 movies
movies = numpy.random.randint(5, size=(3, 1000)) + 1

# Get an array of dot product for movies
dot_products = numpy.dot(user, movies)

print 'the dot products for all movies are', dot_products

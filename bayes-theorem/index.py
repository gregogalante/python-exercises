import pandas as pd

# Bayes Theorem:
# P(H|D) = P(D|H) * P(H) / P(D)

# Read titanic survivors from CSV
titanic = pd.read_csv('titanic.csv')
titanic.head()

num_rows = float(titanic.shape[0])

# Calculate probability for survived and complementary
p_survived = (titanic.Survived == 'yes').sum() / num_rows
p_not_survived = 1 - p_survived

# Calculate probability for male and complementary
p_male = (titanic.Sex == 'male').sum() / num_rows
p_female = 1 - p_male

# TODO: Continue

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

# Calculate probability to survive for a female
# P(Survived|Female) = P(Female|Survived) * P(Survived) / P(Female)
#                    = P(Female AND Survived) / P(Female)
num_female = titanic[titanic.Sex == 'female'].shape[0]
survived_female = titanic[(titanic.Sex == 'female') & (titanic.Survived == 'yes')].shape[0]
p_survived_female = survived_female / float(num_female)

print 'Probability to survive for a female:', p_survived_female

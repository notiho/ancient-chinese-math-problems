"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five people dividing five qian (units of money). 
The condition is that the amount received by the first two people (the "upper two") should equal the amount received by the last three people (the "lower three").
Question: how much does each person receive?

The procedure says: Arrange the qian in a decreasing sequence. Combine the upper two people into 9 and the lower three people into 6. 
The difference between 6 and 9 is 3. Distribute this difference evenly, and add it back. 
Combine all into the divisor. Multiply the total qian by the uncombined values for each person to get the dividend. 
Divide the dividend by the divisor to get the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, and Person E gets *e* qian.
"""

from fractions import Fraction

# Total qian to be divided
total_qian = 5

# Initial arrangement of weights (錢錐行衰)
weights = [5, 4, 1, 1, 1]  # Upper two: 5, 4; Lower three: 1, 1, 1

# Combine the upper two and lower three
upper_two = weights[0] + weights[1]  # 5 + 4 = 9
lower_three = weights[2] + weights[3] + weights[4]  # 1 + 1 + 1 = 3

# Difference between upper two and lower three
difference = upper_two - lower_three  # 9 - 6 = 3

# Distribute the difference evenly and adjust weights
adjustment = difference / 3  # 3 / 3 = 1
weights[2] += adjustment
weights[3] += adjustment
weights[4] += adjustment

# Combine all weights into the divisor (法)
法 = sum(weights)

# Calculate the dividend (實) for each person
實 = [total_qian * weight for weight in weights]

# Divide each dividend by the divisor to get the qian for each person
a, b, c, d, e = [Fraction(實[i], 法) for i in range(5)]

# Output the results
a, b, c, d, e#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

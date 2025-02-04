"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (units of money). 
The condition is that the amount obtained by the first two people (upper group) is equal to the amount obtained by the last three people (lower group).
Question: how much does each person get?

The procedure says: Arrange the qian in a tapered sequence. Combine the upper two people into 9, and the lower three people into 6. 
The difference between 6 and 9 is 3. Distribute this difference equally among the groups, and add it back. 
Combine the totals to form the divisor. Multiply the total qian by the uncombined values for each person to form the dividend. 
Divide the dividend by the divisor to obtain the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, and Person E gets *e* qian.
"""

from fractions import Fraction

# Total qian to be divided
total_qian = 5

# Initial weights for the 5 people
weights = [5, 4, 3, 2, 1]

# Combine the upper two people (weights 5 + 4) and the lower three people (weights 3 + 2 + 1)
upper_sum = weights[0] + weights[1]  # 5 + 4 = 9
lower_sum = weights[2] + weights[3] + weights[4]  # 3 + 2 + 1 = 6

# Difference between upper and lower groups
difference = upper_sum - lower_sum  # 9 - 6 = 3

# Adjust the weights by distributing the difference equally
adjustment = difference / len(weights)  # 3 / 5 = 0.6
adjusted_weights = [w - adjustment for w in weights]

# Combine adjusted weights to form the divisor
divisor = sum(adjusted_weights)

# Multiply total qian by each adjusted weight to form the dividend
dividends = [total_qian * w for w in adjusted_weights]

# Divide each dividend by the divisor to get the qian for each person
results = [Fraction(d, divisor) for d in dividends]

# Assign results to each person
a, b, c, d, e = results

# Output
a, b, c, d, e#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

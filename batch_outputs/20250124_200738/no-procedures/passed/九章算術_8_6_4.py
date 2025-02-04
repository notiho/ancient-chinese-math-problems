"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

#----- content starts here -----
"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
Also, 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is one cow worth, and how much is one sheep worth?

Answer: one cow is worth *a* liang of gold, and one sheep is worth *b* liang of gold.
"""

# Let the value of one cow be x (in liang) and the value of one sheep be y (in liang).
# We have the following equations:
# 5x + 2y = 10
# 2x + 5y = 8

from fractions import Fraction

# Solve the system of equations using substitution or elimination.
# Multiply the first equation by 5 and the second equation by 2 to align coefficients of y:
# 25x + 10y = 50
# 4x + 10y = 16

# Subtract the second equation from the first:
# (25x + 10y) - (4x + 10y) = 50 - 16
# 21x = 34
x = Fraction(34, 21)  # Value of one cow (a)

# Substitute x into the first equation to solve for y:
# 5x + 2y = 10
# 5(Fraction(34, 21)) + 2y = 10
# Fraction(170, 21) + 2y = 10
# 2y = 10 - Fraction(170, 21)
# 2y = Fraction(210, 21) - Fraction(170, 21)
# 2y = Fraction(40, 21)
y = Fraction(20, 21)  # Value of one sheep (b)

# Final results
a = x  # Value of one cow
b = y  # Value of one sheep

a, b  # Output the results#----- content ends here -----

"""
"""

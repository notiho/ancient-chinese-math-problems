"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

#----- content starts here -----
"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
Also, 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is one cow and one sheep worth respectively?

Answer: one cow is worth *a* liang of gold, and one sheep is worth *b* liang of gold.
"""

from fractions import Fraction

# Let x = price of one cow, y = price of one sheep
# Equation 1: 5x + 2y = 10
# Equation 2: 2x + 5y = 8

# Solve for x and y using substitution or elimination
# Multiply Equation 1 by 5 and Equation 2 by 2 to eliminate y:
# 25x + 10y = 50
# 4x + 10y = 16

# Subtract the second equation from the first:
# (25x + 10y) - (4x + 10y) = 50 - 16
# 21x = 34
x = Fraction(34, 21)  # Price of one cow

# Substitute x back into Equation 1 to solve for y:
# 5x + 2y = 10
# 2y = 10 - 5x
# y = (10 - 5x) / 2
y = Fraction(10 - 5 * x, 2)  # Price of one sheep

# Results
a = x  # Price of one cow
b = y  # Price of one sheep

a, b  # Output the results#----- content ends here -----

"""
"""

"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
And 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is one cow and one sheep worth respectively?

Answer: one cow is worth *a* liang of gold, and one sheep is worth *b* liang of gold.
"""

# Let the price of one cow be x (in liang) and one sheep be y (in liang)
# We have the following equations:
# 5x + 2y = 10
# 2x + 5y = 8

# Solve for x (price of one cow) and y (price of one sheep)
from fractions import Fraction

# Multiply the first equation by 5 and the second by 2 to eliminate y
# 25x + 10y = 50
# 4x + 10y = 16

# Subtract the second equation from the first
# 25x - 4x = 50 - 16
x = Fraction(34, 21)  # Price of one cow

# Substitute x into the first equation to solve for y
# 5x + 2y = 10
y = Fraction(10 - 5 * x, 2)  # Price of one sheep

# Final results
a = x  # Price of one cow
b = y  # Price of one sheep

a, b  # Output the results
"""
"""

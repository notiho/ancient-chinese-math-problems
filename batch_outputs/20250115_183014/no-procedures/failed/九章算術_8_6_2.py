"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
And 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is each cow and each sheep worth?

Answer: each cow is worth *a* gold, and *b* liang of gold. Each sheep is worth *c* gold, and *d* liang of gold.
"""

# Let the value of a cow be x and the value of a sheep be y.
# We have the following system of equations:
# 5x + 2y = 10
# 2x + 5y = 8

# Solve for x (value of a cow) and y (value of a sheep) using substitution or elimination.

from fractions import Fraction

# Equation 1: 5x + 2y = 10
# Equation 2: 2x + 5y = 8

# Multiply Equation 1 by 2 and Equation 2 by 5 to eliminate x:
# 10x + 4y = 20
# 10x + 25y = 40

# Subtract the first from the second:
# (10x + 25y) - (10x + 4y) = 40 - 20
# 21y = 20
y = Fraction(20, 21)  # Value of a sheep

# Substitute y back into Equation 1 to solve for x:
# 5x + 2y = 10
# 5x + 2 * (20/21) = 10
# 5x + 40/21 = 10
# 5x = 10 - 40/21
# 5x = (210/21) - (40/21)
# 5x = 170/21
x = Fraction(170, 105)  # Value of a cow

# Final results:
a = x.numerator
b = x.denominator
c = y.numerator
d = y.denominator
"""
Variable 'a' has wrong value. Expected: 1, Actual: 34
Variable 'b' has wrong value. Expected: 34/21, Actual: 21
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 20/21, Actual: 21"""

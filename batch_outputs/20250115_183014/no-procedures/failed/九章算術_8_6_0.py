"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
And 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: How much is each cow and each sheep worth?

Answer: Each cow is worth *a* gold, *b* liang, and each sheep is worth *c* gold, *d* liang.
"""

# Let the value of a cow be x (in liang) and the value of a sheep be y (in liang).
# We have the following system of equations:
# 5x + 2y = 10
# 2x + 5y = 8

from fractions import Fraction

# Solve for x (value of a cow) and y (value of a sheep)
# Multiply the first equation by 5 and the second equation by 2 to eliminate y:
# 25x + 10y = 50
# 4x + 10y = 16

# Subtract the second equation from the first:
# 25x - 4x = 50 - 16
x = Fraction(34, 21)  # Value of a cow in liang

# Substitute x back into the first equation to solve for y:
# 5x + 2y = 10
y = Fraction(10 - 5 * x, 2)  # Value of a sheep in liang

# Assign the results
a = x.numerator
b = x.denominator
c = y.numerator
d = y.denominator

# Results:
# Each cow is worth a/b liang.
# Each sheep is worth c/d liang.
"""
Variable 'a' has wrong value. Expected: 1, Actual: 34
Variable 'b' has wrong value. Expected: 34/21, Actual: 21
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 20/21, Actual: 21"""

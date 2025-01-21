"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
Also, 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is each cow and each sheep worth?

Answer: each cow is worth *a* gold, *b* liang, and each sheep is worth *c* gold, *d* liang.
"""

from fractions import Fraction

# Let the price of a cow be x and the price of a sheep be y.
# We have the following system of equations:
# 5x + 2y = 10
# 2x + 5y = 8

# Solve for x (price of a cow) and y (price of a sheep) using substitution or elimination.

# Multiply the first equation by 5 and the second equation by 2 to align coefficients of y:
# 25x + 10y = 50
# 4x + 10y = 16

# Subtract the second equation from the first:
# (25x + 10y) - (4x + 10y) = 50 - 16
# 21x = 34
x = Fraction(34, 21)  # Price of a cow

# Substitute x into the first equation to solve for y:
# 5x + 2y = 10
# 2y = 10 - 5x
# y = (10 - 5x) / 2
y = Fraction(10 - 5 * x, 2)  # Price of a sheep

# Final results:
a = x.numerator  # Numerator of cow price
b = x.denominator  # Denominator of cow price
c = y.numerator  # Numerator of sheep price
d = y.denominator  # Denominator of sheep price

# Results:
# Cow price: a/b liang
# Sheep price: c/d liang
"""
Variable 'a' has wrong value. Expected: 1, Actual: 34
Variable 'b' has wrong value. Expected: 34/21, Actual: 21
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 20/21, Actual: 21"""

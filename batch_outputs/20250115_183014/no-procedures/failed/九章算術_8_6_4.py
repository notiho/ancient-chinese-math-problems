"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
Suppose there are 2 cows and 5 sheep worth a total of 8 liang of gold.
Question: how much is each cow and each sheep worth?

Answer: each cow is worth *a* liang of gold, and the total for cows is *b* liang. Each sheep is worth *c* liang of gold, and the total for sheep is *d* liang.
"""

# Let the price of a cow be x and the price of a sheep be y
# We have the following system of equations:
# 5x + 2y = 10
# 2x + 5y = 8

from fractions import Fraction

# Solve for x (price of a cow) and y (price of a sheep)
# Multiply the first equation by 5 and the second by 2 to eliminate y
# 25x + 10y = 50
# 4x + 10y = 16
# Subtract the second equation from the first
# 21x = 34
x = Fraction(34, 21)  # Price of a cow

# Substitute x into the first equation to solve for y
# 5x + 2y = 10
# 2y = 10 - 5x
# y = (10 - 5x) / 2
y = Fraction(10 - 5 * x, 2)  # Price of a sheep

# Calculate the total value for cows and sheep
a = x  # Price of one cow
b = 5 * x  # Total value of cows
c = y  # Price of one sheep
d = 2 * y  # Total value of sheep

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 170/21
Variable 'c' has wrong value. Expected: 1, Actual: 20/21
Variable 'd' has wrong value. Expected: 20/21, Actual: 40/21"""

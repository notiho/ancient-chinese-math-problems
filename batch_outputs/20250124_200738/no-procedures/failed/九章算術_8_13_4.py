"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

#----- content starts here -----
"""
Suppose there are four types of grain: white grain (2 bu), green grain (3 bu), yellow grain (4 bu), and black grain (5 bu). Each type of grain is not enough to fill one dou on its own. 

White grain takes 1 bu each from green and yellow.
Green grain takes 1 bu each from yellow and black.
Yellow grain takes 1 bu each from black and white.
Black grain takes 1 bu each from white and green.

After these exchanges, each type of grain fills exactly 1 dou. 

Question: How much does 1 bu of each type of grain contribute to the total volume?

Answer: White grain contributes *a* dou per bu, green grain contributes *b* dou per bu, yellow grain contributes *c* dou per bu, and black grain contributes *d* dou per bu.
"""

from fractions import Fraction

# Define the total volume of each type of grain (in bu)
白禾 = 2
青禾 = 3
黃禾 = 4
黑禾 = 5

# Define the equations based on the problem:
# White grain + 1 bu from green + 1 bu from yellow = 1 dou
# Green grain + 1 bu from yellow + 1 bu from black = 1 dou
# Yellow grain + 1 bu from black + 1 bu from white = 1 dou
# Black grain + 1 bu from white + 1 bu from green = 1 dou

# Let the contribution of 1 bu of each type of grain be:
# 白禾一步實 = a dou
# 青禾一步實 = b dou
# 黃禾一步實 = c dou
# 黑禾一步實 = d dou

# Set up the equations:
# 2a + b + c = 1
# 3b + c + d = 1
# 4c + d + a = 1
# 5d + a + b = 1

# Solve the system of equations manually:
# From the first equation: b + c = 1 - 2a
# From the second equation: c + d = 1 - 3b
# From the third equation: d + a = 1 - 4c
# From the fourth equation: a + b = 1 - 5d

# Substitute and solve step by step:
# From b + c = 1 - 2a, we get b = 1 - 2a - c
# Substitute b into c + d = 1 - 3b:
# c + d = 1 - 3(1 - 2a - c)
# c + d = 1 - 3 + 6a + 3c
# d = 6a + 2c - 2

# Substitute d into d + a = 1 - 4c:
# (6a + 2c - 2) + a = 1 - 4c
# 7a + 6c = 3
# c = (3 - 7a) / 6

# Substitute c into a + b = 1 - 5d:
# a + (1 - 2a - c) = 1 - 5(6a + 2c - 2)
# a + 1 - 2a - c = 1 - 30a - 10c + 10
# -a - c = -30a - 10c + 10
# 29a = 9c + 10
# Substitute c = (3 - 7a) / 6 into 29a = 9c + 10:
# 29a = 9((3 - 7a) / 6) + 10
# 29a = (27 - 63a) / 6 + 10
# 174a = 27 - 63a + 60
# 237a = 87
# a = 87 / 237 = 29 / 79

# Solve for b, c, and d:
a = Fraction(29, 79)
c = Fraction(3 - 7 * a, 6)
b = Fraction(1 - 2 * a - c)
d = Fraction(6 * a + 2 * c - 2)

# Final results:
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 29/79
Variable 'b' has wrong value. Expected: 28/111, Actual: 46/237
Variable 'c' has wrong value. Expected: 17/111, Actual: 17/237
Variable 'd' has wrong value. Expected: 10/111, Actual: 82/237"""

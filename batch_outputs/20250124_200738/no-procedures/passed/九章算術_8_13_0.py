"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

#----- content starts here -----
"""
Suppose there are four types of grain: white grain (2 bu), green grain (3 bu), yellow grain (4 bu), and black grain (5 bu). Each type of grain is less than 1 dou in volume. 
White grain takes 1 bu each from green and yellow; green grain takes 1 bu each from yellow and black; yellow grain takes 1 bu each from black and white; black grain takes 1 bu each from white and green. After this exchange, each type of grain becomes exactly 1 dou in volume.

Question: What is the volume of 1 bu of each type of grain?

Answer: White grain 1 bu is *a* dou, green grain 1 bu is *b* dou, yellow grain 1 bu is *c* dou, black grain 1 bu is *d* dou.
"""

# Let the volume of 1 bu of each type of grain be variables:
# 白禾一步實 a斗
# 青禾一步實 b斗
# 黃禾一步實 c斗
# 黑禾一步實 d斗

# Total volume equations after exchange:
# White grain: 2a + b + c = 1
# Green grain: 3b + c + d = 1
# Yellow grain: 4c + d + a = 1
# Black grain: 5d + a + b = 1

from fractions import Fraction

# Solve the equations step by step
# From the first equation: b + c = 1 - 2a
# From the second equation: c + d = 1 - 3b
# From the third equation: d + a = 1 - 4c
# From the fourth equation: a + b = 1 - 5d

# Substitute and solve:
# From b + c = 1 - 2a, we get b = 1 - 2a - c
# Substitute b into a + b = 1 - 5d:
# a + (1 - 2a - c) = 1 - 5d
# 1 - a - c = 1 - 5d
# a + c = 5d  ---- (1)

# From c + d = 1 - 3b, substitute b = 1 - 2a - c:
# c + d = 1 - 3(1 - 2a - c)
# c + d = 1 - 3 + 6a + 3c
# d = 6a + 2c - 2 ---- (2)

# From d + a = 1 - 4c, substitute d = 6a + 2c - 2:
# (6a + 2c - 2) + a = 1 - 4c
# 7a + 2c - 2 = 1 - 4c
# 7a + 6c = 3
# a = (3 - 6c) / 7 ---- (3)

# Substitute a = (3 - 6c) / 7 into (1):
# (3 - 6c) / 7 + c = 5d
# (3 - 6c + 7c) / 7 = 5d
# (3 + c) / 7 = 5d
# d = (3 + c) / 35 ---- (4)

# Substitute a = (3 - 6c) / 7 and d = (3 + c) / 35 into (2):
# d = 6a + 2c - 2
# (3 + c) / 35 = 6((3 - 6c) / 7) + 2c - 2
# (3 + c) / 35 = (18 - 36c) / 7 + 2c - 2
# (3 + c) / 35 = (90 - 180c + 70c - 70) / 35
# 3 + c = 90 - 110c - 70
# 3 + c = 20 - 110c
# 111c = 17
# c = 17 / 111 ---- (5)

# Substitute c = 17 / 111 into a = (3 - 6c) / 7:
a = Fraction(3 - 6 * Fraction(17, 111), 7)

# Substitute c = 17 / 111 into d = (3 + c) / 35:
d = Fraction(3 + Fraction(17, 111), 35)

# Substitute a and c into b = 1 - 2a - c:
b = 1 - 2 * a - Fraction(17, 111)

# Final results:
a = a
b = b
c = Fraction(17, 111)
d = d

a, b, c, d#----- content ends here -----

"""
"""

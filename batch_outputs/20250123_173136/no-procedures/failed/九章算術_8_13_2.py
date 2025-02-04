"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
Suppose there are four types of grain: white grain (2 bu), green grain (3 bu), yellow grain (4 bu), and black grain (5 bu). Each type of grain is less than 1 dou in volume. 

White grain takes 1 bu each from green and yellow grain, green grain takes 1 bu each from yellow and black grain, yellow grain takes 1 bu each from black and white grain, and black grain takes 1 bu each from white and green grain. After these exchanges, each type of grain becomes exactly 1 dou.

Question: What is the volume of 1 bu of white, green, yellow, and black grain respectively?

Answer: White grain per bu is *a* dou, green grain per bu is *b* dou, yellow grain per bu is *c* dou, and black grain per bu is *d* dou.
"""

from fractions import Fraction

# Let the volume of 1 bu of white, green, yellow, and black grain be a, b, c, and d respectively.
# We know the following equations based on the problem:

# White grain: 2a + b + c = 1
# Green grain: 3b + c + d = 1
# Yellow grain: 4c + d + a = 1
# Black grain: 5d + a + b = 1

# Solve the system of equations step by step.

# From the first equation: b + c = 1 - 2a
# From the second equation: c + d = 1 - 3b
# From the third equation: d + a = 1 - 4c
# From the fourth equation: a + b = 1 - 5d

# Substitute step by step to solve for a, b, c, and d.

# Step 1: Express b in terms of a and c
b = 1 - 2 * a - c

# Step 2: Express d in terms of b and c
d = 1 - 3 * b - c

# Step 3: Substitute b into d
d = 1 - 3 * (1 - 2 * a - c) - c
d = 1 - 3 + 6 * a + 3 * c - c
d = -2 + 6 * a + 2 * c

# Step 4: Substitute d into the third equation to solve for c
# d + a = 1 - 4c
(-2 + 6 * a + 2 * c) + a = 1 - 4 * c
-2 + 7 * a + 2 * c = 1 - 4 * c
7 * a + 6 * c = 3
c = Fraction(3 - 7 * a, 6)

# Step 5: Substitute c into b
b = 1 - 2 * a - c
b = 1 - 2 * a - Fraction(3 - 7 * a, 6)
b = Fraction(6 - 12 * a - (3 - 7 * a), 6)
b = Fraction(6 - 12 * a - 3 + 7 * a, 6)
b = Fraction(3 - 5 * a, 6)

# Step 6: Substitute c into d
d = -2 + 6 * a + 2 * c
d = -2 + 6 * a + 2 * Fraction(3 - 7 * a, 6)
d = -2 + 6 * a + Fraction(6 - 14 * a, 6)
d = Fraction(-12 + 36 * a + 6 - 14 * a, 6)
d = Fraction(-6 + 22 * a, 6)

# Step 7: Substitute c into a
a,b
"""
Code error: cannot assign to expression here. Maybe you meant '==' instead of '='? (<string>, line 44)"""

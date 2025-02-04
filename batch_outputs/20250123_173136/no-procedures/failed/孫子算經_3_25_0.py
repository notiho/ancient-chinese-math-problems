"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
答曰： a 獸 b 禽。
"""

"""
Suppose there are beasts (each with 6 heads and 4 legs) and birds (each with 2 heads and 2 legs).
In total, there are 76 heads and 46 legs.
Question: how many beasts and birds are there?

Answer: there are *a* beasts and *b* birds.
"""

# Define the total number of heads and legs
total_heads = 76
total_legs = 46

# Let the number of beasts be x and the number of birds be y
# Each beast has 6 heads and 4 legs
# Each bird has 2 heads and 2 legs
# We solve the system of equations:
# 6x + 2y = total_heads
# 4x + 2y = total_legs

# Subtract the second equation from the first to eliminate y
# (6x + 2y) - (4x + 2y) = total_heads - total_legs
# 2x = total_heads - total_legs
x = (total_heads - total_legs) // 2  # Number of beasts

# Substitute x into the second equation to solve for y
# 4x + 2y = total_legs
# 2y = total_legs - 4x
y = (total_legs - 4 * x) // 2  # Number of birds

# Assign the results
a = x  # Number of beasts
b = y  # Number of birds

# Final result
a, b
"""
Variable 'a' has wrong value. Expected: 8, Actual: 15
Variable 'b' has wrong value. Expected: 7, Actual: -7"""

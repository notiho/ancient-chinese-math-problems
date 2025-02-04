"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a total volume of 1,860,867 cubic chi (尺³).
Question: how many chi (尺) is the side length of the cube?

Answer: the side length is *a* chi.
"""

# Given total volume
積 = 1860867

# To find the side length of the cube, we need to compute the cube root of the volume.
# We will approximate the cube root manually using integer arithmetic.

# Start with an initial guess for the cube root
a = 0

# Incrementally find the largest integer `a` such that a³ ≤ 積
while a**3 <= 積:
    a += 1

# The result is one step too high, so subtract 1
a -= 1

# Final result
a#----- content ends here -----

"""
"""

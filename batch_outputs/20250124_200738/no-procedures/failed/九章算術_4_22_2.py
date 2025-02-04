"""
今有積四千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 4500 cubic chi (尺³). It is desired to find the diameter of a cylinder with this volume.
Question: what is the diameter?

Answer: the diameter is *a* chi.
"""

# Given volume
積 = 4500

# Formula for the volume of a cylinder: V = (π * r^2 * h)
# Here, we assume the height (h) equals the diameter (d), so V = (π * (d/2)^2 * d)
# Simplify: V = (π * d^3) / 4
# Solve for d: d = (4 * V / π)^(1/3)

# Using π as 3 for simplicity (as was common in ancient Chinese mathematics)
π = 3

# Solve for diameter
a = Fraction(4 * 積, π) ** Fraction(1, 3)  # Cube root of (4 * V / π)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 20, Actual: 18.171205928321395"""

"""
今有積四千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 4500 cubic chi (尺³).
Question: what is the diameter of a cylinder with this volume?

Answer: the diameter is *a* chi.
"""

# 積四千五百尺
積 = 4500

# Formula for the volume of a cylinder: V = (π * r^2 * h)
# Here, we assume the height (h) is equal to the diameter (d), so h = d.
# Substituting h = d, the formula becomes: V = (π * (d/2)^2 * d) = (π * d^3) / 4
# Rearranging to solve for d: d³ = (4 * V) / π

# Using π ≈ 3 for simplicity (as was common in ancient Chinese calculations)
pi = 3

# Solve for diameter (d)
a = Fraction((4 * 積), pi) ** Fraction(1, 3)  # Cube root of (4 * V / π)
"""
Variable 'a' has wrong value. Expected: 20, Actual: 18.171205928321395"""

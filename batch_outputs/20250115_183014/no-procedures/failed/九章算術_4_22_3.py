"""
今有積四千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 4500 cubic chi. It is desired to form a cylinder.
Question: what is the diameter of the base of the cylinder?

Answer: the diameter is *a* chi.
"""

# 積四千五百尺
積 = 4500

# Formula for the volume of a cylinder: V = π * (d/2)^2 * h
# Assume the height (h) of the cylinder is equal to its diameter (d), i.e., h = d.
# Then, V = π * (d/2)^2 * d = (π/4) * d^3
# Solve for d: d^3 = (4 * V) / π

# Using π ≈ 3 for simplicity in ancient Chinese calculations
pi = 3

# Solve for d
a = Fraction(4 * 積, pi) ** Fraction(1, 3)  # Cube root of (4 * V / π)

# Note: In ancient Chinese math, cube roots were often approximated manually.
"""
Variable 'a' has wrong value. Expected: 20, Actual: 18.171205928321395"""

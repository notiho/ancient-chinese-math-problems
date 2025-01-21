"""
今有積四千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 4500 cubic chi. 
Question: what is the diameter of the cylinder (立圓)?

Answer: the diameter is *a* chi.
"""

# Given volume
積 = 4500

# Formula for the volume of a cylinder: V = (π * d^2 * h) / 4
# Assuming the height (h) is equal to the diameter (d), the formula becomes:
# V = (π * d^3) / 4
# Solving for d:
# d^3 = (4 * V) / π
# d = ((4 * V) / π)^(1/3)

# Using π ≈ 3 for ancient Chinese calculations:
pi = 3

# Solve for diameter
a = ((4 * 積) / pi) ** Fraction(1, 3)  # Cube root of (4 * 積 / π)
"""
Variable 'a' has wrong value. Expected: 20, Actual: 18.171205928321395"""

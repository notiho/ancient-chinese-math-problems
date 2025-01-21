"""
今有積四千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 4500 cubic chi (尺³). It is desired to find the diameter of a cylinder with this volume.
Question: what is the diameter?

Answer: the diameter is *a* chi.
"""

# Given volume
積 = 4500

# Formula for the volume of a cylinder: V = (π * r² * h), where r is the radius and h is the height.
# Assume the height (h) is equal to the diameter (d), so h = d.
# Substituting h = d into the formula: V = (π * (d/2)² * d) = (π * d³) / 4
# Rearranging for d: d³ = (4 * V) / π

# Using π ≈ 3 for simplicity (as was common in ancient Chinese mathematics):
pi = 3
d_cubed = (4 * 積) / pi

# Solve for d (diameter):
a = Fraction(d_cubed) ** Fraction(1, 3)  # Cube root of d³ (approximation)
"""
Variable 'a' has wrong value. Expected: 20, Actual: 18.171205928321395"""

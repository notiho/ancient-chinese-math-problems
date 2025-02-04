"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, and the distance from the base of the bamboo to the point where the tip touches the ground is 3 chi.
Question: how tall is the bamboo at the point where it bends?

Answer: *a* chi.
"""

# 竹高一丈 (1丈 = 10尺)
竹高 = 10  # in chi

# 去本三尺
去本 = 3  # in chi

# Using the Pythagorean theorem:
# The bamboo forms a right triangle where:
# - The hypotenuse is the original height of the bamboo (10 chi),
# - One leg is the distance from the base to the tip touching the ground (3 chi),
# - The other leg is the height of the bamboo at the point where it bends (unknown, let's call it `a`).

# Hypotenuse^2 = Leg1^2 + Leg2^2
# 10^2 = 3^2 + a^2
# a^2 = 10^2 - 3^2
# a = sqrt(10^2 - 3^2)

from fractions import Fraction

# Calculate a
a_squared = 竹高**2 - 去本**2
a = Fraction(a_squared).sqrt()

# Result
a#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, and the distance from the base of the bamboo to the point where the tip touches the ground is 3 chi.
Question: how high is the broken part of the bamboo?

Answer: the broken part is *a* chi tall.
"""

# Bamboo height in chi (1 zhang = 10 chi)
竹高 = 10

# Distance from the base to the tip touching the ground
去本 = 3

# Using the Pythagorean theorem:
# The bamboo forms a right triangle where:
# - The original height of the bamboo is the hypotenuse (10 chi),
# - The distance from the base to the tip touching the ground is one leg (3 chi),
# - The height of the broken part is the other leg.

# Let the height of the broken part be `a` and the length of the broken segment be `b`.
# The relationship is:
# a^2 + 去本^2 = 竹高^2

# Solve for `a`:
a = (竹高**2 - 去本**2)**0.5

# Convert to Fraction for exact representation
from fractions import Fraction
a = Fraction(竹高**2 - 去本**2).sqrt()

a#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

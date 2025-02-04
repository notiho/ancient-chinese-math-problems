"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
荅曰： a尺 。
"""

"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, and the distance from the base of the bamboo to the tip on the ground is 3 chi.
Question: how high is the point where the bamboo bends?

Answer: the height of the bending point is *a* chi.
"""

# Bamboo height in chi (1 zhang = 10 chi)
竹高 = 10

# Distance from base to tip on the ground in chi
去本 = 3

# Using the Pythagorean theorem:
# The bamboo forms a right triangle where:
# - The original height of the bamboo is the hypotenuse (10 chi),
# - The distance from the base to the tip on the ground is one leg (3 chi),
# - The remaining height of the bamboo (折者高) is the other leg.

# Hypotenuse^2 = Leg1^2 + Leg2^2
# Leg2^2 = Hypotenuse^2 - Leg1^2
折者高平方 = 竹高**2 - 去本**2

# 折者高 = sqrt(折者高平方)
# Since we are working with exact values, we avoid square roots and simplify:
a = Fraction(折者高平方).limit_denominator()  # Simplified exact value in chi
"""
Variable 'a' has wrong value. Expected: 91/20, Actual: 91"""

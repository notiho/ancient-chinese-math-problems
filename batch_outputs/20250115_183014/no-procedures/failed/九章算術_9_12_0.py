"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
荅曰： a尺 。
"""

"""
Suppose there is a bamboo that is 1 zhang tall. Its top bends and touches the ground, and the distance from the base of the bamboo to the point where the top touches the ground is 3 chi.
Question: how high is the point where the bamboo is bent?

Answer: *a* chi.
"""

# Bamboo height in chi (1 zhang = 10 chi)
竹高 = 10

# Distance from base to where the top touches the ground
去本 = 3

# Using the Pythagorean theorem:
# The bamboo forms a right triangle where:
# - The hypotenuse is the original bamboo height (10 chi),
# - One leg is the distance from the base to the point where the top touches the ground (3 chi),
# - The other leg is the height of the bent bamboo (what we are solving for).

# Hypotenuse squared minus one leg squared equals the other leg squared
a_squared = 竹高**2 - 去本**2

# Take the square root to find the height of the bent bamboo
a = Fraction(a_squared).sqrt()

# Result
a
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

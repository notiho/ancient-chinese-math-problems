"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

"""
Suppose two people start from the same point. Person A walks at a rate of 7 bu per unit time, and Person B walks at a rate of 3 bu per unit time. Person B walks east, while Person A walks south for 10 bu and then walks diagonally northeast to meet Person B.

Question: How far does Person B walk east, and how far does Person A walk diagonally to meet Person B?

Answer: Person B walks *a* bu east, and Person A walks *b* bu diagonally to meet them.
"""

from fractions import Fraction
import math

# Given data
甲行率 = 7  # Person A's rate of walking
乙行率 = 3  # Person B's rate of walking
甲南行 = 10  # Person A walks south for 10 bu

# Let the time it takes for Person A to walk diagonally and meet Person B be t.
# During this time, Person B walks east for a distance of a = 乙行率 * t.
# During this time, Person A walks diagonally for a distance of b = 甲行率 * t.

# The diagonal distance forms a right triangle:
# The southward distance is 10 bu (甲南行), and the eastward distance is a (乙行率 * t).
# The diagonal distance b is the hypotenuse of the triangle.

# Using the Pythagorean theorem:
# b^2 = (甲南行)^2 + (乙行率 * t)^2
# b = 甲行率 * t

# Substituting b = 甲行率 * t into the equation:
# (甲行率 * t)^2 = (甲南行)^2 + (乙行率 * t)^2
# Solve for t:
# (7t)^2 = 10^2 + (3t)^2
# 49t^2 = 100 + 9t^2
# 49t^2 - 9t^2 = 100
# 40t^2 = 100
# t^2 = 100 / 40
# t^2 = 5/2
# t = sqrt(5/2)

t = math.sqrt(Fraction(5, 2))

# Calculate a (distance Person B walks east)
a = 乙行率 * t

# Calculate b (distance Person A walks diagonally)
b = 甲行率 * t

# Final results
a = Fraction(a).limit_denominator()  # Convert to fraction
b = Fraction(b).limit_denominator()  # Convert to fraction

a, b  # Output the results
"""
Variable 'a' has wrong value. Expected: 21/2, Actual: 1039681/219184
Variable 'b' has wrong value. Expected: 29/2, Actual: 1039681/93936"""

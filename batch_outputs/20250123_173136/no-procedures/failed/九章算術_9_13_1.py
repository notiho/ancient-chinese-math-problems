"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

"""
Suppose two people start at the same point. Person A walks at a rate of 7 bu per unit time, and Person B walks at a rate of 3 bu per unit time. Person B walks east, while Person A walks south for 10 bu and then walks diagonally northeast to meet Person B.

Question: How far does Person B walk east, and how far does Person A walk diagonally to meet Person B?

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally to meet them.
"""

from fractions import Fraction
import math

# 甲行率 (Person A's speed)
甲行率 = 7

# 乙行率 (Person B's speed)
乙行率 = 3

# 甲南行十步 (Person A walks south for 10 bu)
甲南行 = 10

# Let the time it takes for Person A to walk diagonally and meet Person B be t.
# During this time, Person B walks east, and Person A walks diagonally northeast.

# The distance Person B walks east is:
# a = 乙行率 * t

# The diagonal distance Person A walks is:
# b = 甲行率 * t

# The diagonal path forms a right triangle:
# - The vertical leg is 甲南行 (10 bu),
# - The horizontal leg is a (乙行率 * t),
# - The hypotenuse is b (甲行率 * t).

# Using the Pythagorean theorem:
# (甲行率 * t)^2 = (乙行率 * t)^2 + 甲南行^2

# Solve for t:
# t^2 * (甲行率^2 - 乙行率^2) = 甲南行^2
# t^2 = 甲南行^2 / (甲行率^2 - 乙行率^2)
# t = sqrt(甲南行^2 / (甲行率^2 - 乙行率^2))

t_squared = Fraction(甲南行**2, 甲行率**2 - 乙行率**2)
t = math.sqrt(t_squared)

# Calculate a and b:
a = Fraction(乙行率) * t
b = Fraction(甲行率) * t

# Results:
a, b
"""
Variable 'a' has wrong value. Expected: 21/2, Actual: 4.743416490252569
Variable 'b' has wrong value. Expected: 29/2, Actual: 11.067971810589329"""

"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

#----- content starts here -----
"""
Suppose two people start from the same point. Person A walks at a rate of 7 (steps per unit time), and Person B walks at a rate of 3 (steps per unit time). Person B walks east, while Person A walks south for 10 steps and then diagonally northeast to meet Person B. 

Question: How far does Person B walk east, and how far does Person A walk diagonally to meet Person B?

Answer: Person B walks *a* steps east; Person A walks *b* steps diagonally to meet them.
"""

from fractions import Fraction
import math

# Given data
甲行率 = 7  # Person A's walking rate
乙行率 = 3  # Person B's walking rate
甲南行 = 10  # Person A walks 10 steps south

# Let the time it takes for Person A to walk diagonally and meet Person B be t
# During this time, Person B walks east for a distance of 乙行率 * t
# During this time, Person A walks diagonally for a distance of 甲行率 * t

# The diagonal distance forms a right triangle with:
# - One leg being the 10 steps south that Person A initially walked
# - The other leg being the distance Person B walked east (乙行率 * t)
# - The hypotenuse being the diagonal distance Person A walked (甲行率 * t)

# Using the Pythagorean theorem:
# (甲行率 * t)^2 = (乙行率 * t)^2 + 10^2

# Solve for t:
t = Fraction(10, math.sqrt(甲行率**2 - 乙行率**2))

# Calculate the distances:
a = 乙行率 * t  # Distance Person B walks east
b = 甲行率 * t  # Distance Person A walks diagonally

# Results
a = Fraction(a).limit_denominator()  # Convert to a fraction
b = Fraction(b).limit_denominator()  # Convert to a fraction

a, b  # Output the results#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

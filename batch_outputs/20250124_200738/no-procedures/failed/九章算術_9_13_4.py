"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

#----- content starts here -----
"""
Suppose two people start from the same point. Person A walks at a rate of 7 bu per unit time, and Person B walks at a rate of 3 bu per unit time. 
Person B walks east, while Person A walks south for 10 bu and then walks diagonally northeast to meet Person B.
Question: How far does Person B walk east, and how far does Person A walk diagonally to meet Person B?

Answer: Person B walks *a* bu east; Person A walks *b* bu diagonally to meet them.
"""

from fractions import Fraction
import math

# Rates of movement
甲行率 = 7  # Person A's rate (bu per unit time)
乙行率 = 3  # Person B's rate (bu per unit time)

# Person A walks south for 10 bu
甲南行 = 10

# Let the time for Person A's diagonal walk be t
# During this time, Person A walks diagonally northeast at a rate of 7 bu per unit time.
# During the same time, Person B walks east at a rate of 3 bu per unit time.

# The diagonal distance Person A walks is 7 * t
# The eastward distance Person B walks is 3 * t

# The diagonal walk forms a right triangle:
# - One leg is the 10 bu Person A walked south.
# - The other leg is the eastward distance Person B walked (3 * t).
# - The hypotenuse is the diagonal distance Person A walked (7 * t).

# Using the Pythagorean theorem:
# (10)^2 + (3 * t)^2 = (7 * t)^2

# Solve for t:
# 100 + 9 * t^2 = 49 * t^2
# 100 = 40 * t^2
# t^2 = 100 / 40
# t = sqrt(100 / 40)

t = math.sqrt(Fraction(100, 40))

# Calculate the distances:
a = 乙行率 * t  # Distance Person B walks east
b = 甲行率 * t  # Distance Person A walks diagonally

# Results
a = Fraction(a).limit_denominator()  # Convert to fraction
b = Fraction(b).limit_denominator()  # Convert to fraction

a, b  # Output the results#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21/2, Actual: 1039681/219184
Variable 'b' has wrong value. Expected: 29/2, Actual: 1039681/93936"""

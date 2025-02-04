"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

"""
Suppose two people start at the same point. Person A walks at a rate of 7 bu per unit time, and Person B walks at a rate of 3 bu per unit time. Person B walks east, while Person A walks south for 10 bu and then diagonally northeast to meet Person B. 

Question: How far does Person B walk east, and how far does Person A walk diagonally to meet Person B?

Answer: Person B walks *a* bu east, and Person A walks *b* bu diagonally.
"""

from fractions import Fraction
import math

# Rates of walking
甲行率 = 7  # Person A's walking rate
乙行率 = 3  # Person B's walking rate

# 甲南行十步 (Person A walks south for 10 bu)
甲南行 = 10

# Let 乙東行 = a (distance Person B walks east)
# Let 甲邪行 = b (distance Person A walks diagonally)

# Time taken by both to meet is the same
# Time = Distance / Rate
# Time for Person B: a / 乙行率
# Time for Person A: b / 甲行率

# From the geometry of the problem:
# b^2 = (甲南行)^2 + (a)^2 (Pythagoras theorem for diagonal movement)

# Solve for a and b
# Time equality: a / 乙行率 = b / 甲行率
# => a / 3 = b / 7
# => b = (7/3) * a

# Substitute b into the Pythagoras equation:
# b^2 = (甲南行)^2 + a^2
# ((7/3) * a)^2 = (10)^2 + a^2
# (49/9) * a^2 = 100 + a^2
# (49/9) * a^2 - a^2 = 100
# (49/9 - 9/9) * a^2 = 100
# (40/9) * a^2 = 100
# a^2 = (100 * 9) / 40
# a^2 = 900 / 40
# a^2 = 45/2
# a = sqrt(45/2)

# Calculate a
a = Fraction(45, 2).sqrt()

# Calculate b
b = Fraction(7, 3) * a

# Final results
a = Fraction(math.sqrt(45 / 2))
b = Fraction
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

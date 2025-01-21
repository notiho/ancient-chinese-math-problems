"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
Suppose there is a square city with sides of 10 li, and gates are located at the middle of each side.
Both Person A (甲) and Person B (乙) start from the center of the city and leave through different gates.
乙 exits through the east gate, while 甲 exits through the south gate. After exiting, 甲 walks diagonally northeast along the city's boundary and meets 乙.
The ratio of their walking speeds is 甲:乙 = 5:3.

Question: How far does 甲 walk south to the gate, how far does 甲 walk diagonally northeast, and how far does 乙 walk east?

Answer: 甲 walks *a* bu south to the gate, *b* bu diagonally northeast, and 乙 walks *c* bu east.
"""

from fractions import Fraction

# City dimensions
city_side = 10  # li

# Speed ratio of 甲 to 乙
甲_speed = 5
乙_speed = 3

# Distance from the center to the south gate or east gate
a = Fraction(city_side, 2)  # 甲 walks south to the gate (half the city's side)

# Let b be the diagonal distance 甲 walks northeast, and c be the distance 乙 walks east.
# Using the Pythagorean theorem:
# The total distance 甲 travels is the hypotenuse of a right triangle where:
# - One leg is the distance 甲 walks south (a = city_side / 2)
# - The other leg is the distance 乙 walks east (c)

# The relationship between their distances is based on their speed ratio:
# b / c = 甲_speed / 乙_speed = 5 / 3
# Thus, b = (5 / 3) * c

# Using the Pythagorean theorem:
# (city_side / 2)^2 + c^2 = b^2
# Substituting b = (5 / 3) * c:
# (city_side / 2)^2 + c^2 = ((5 / 3) * c)^2

# Solve for c:
a_squared = (city_side / 2) ** 2
c = Fraction(a_squared, (25 / 9) - 1).sqrt()

# Solve for b:
b = Fraction(5, 3) * c

# Final answers:
a = Fraction(city_side, 2)  # Distance 甲 walks south
b = b  # Distance 甲 walks diagonally northeast
c = c  # Distance 乙 walks east

a, b, c
"""
Code error: both arguments should be Rational instances"""

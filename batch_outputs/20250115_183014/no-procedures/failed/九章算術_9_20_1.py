"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Person A and Person B both start from the center of the city. Person B exits through the east gate, while Person A exits through the south gate. After exiting, Person A walks diagonally northeast along the city boundary and meets Person B. The walking speeds of A and B are such that A walks 5 steps for every 3 steps of B.

Question: How far does Person A walk south to the gate, how far does Person A walk diagonally northeast, and how far does Person B walk east?

Answer: Person A walks *a* bu south to the gate, *b* bu diagonally northeast, and Person B walks *c* bu east.
"""

from fractions import Fraction

# City dimensions
city_side = 10  # in li

# Conversion: 1 li = 300 bu
city_side_bu = city_side * 300  # in bu

# Speed ratio: A walks 5 steps for every 3 steps of B
speed_ratio_A_to_B = Fraction(5, 3)

# Let the distance Person B walks east be `c` bu
# Then Person A walks diagonally northeast for `b = (5/3) * c` bu
# Using the Pythagorean theorem:
# (Distance A walks south)^2 + (Distance A walks diagonally northeast)^2 = (Distance B walks east)^2
# a^2 + b^2 = c^2
# a = city_side_bu / 2 (distance A walks south to the gate)

a = city_side_bu // 2  # Distance A walks south to the gate in bu

# Let c = distance B walks east
# b = (5/3) * c
# Using the Pythagorean theorem:
# a^2 + b^2 = c^2
# Substitute b = (5/3) * c:
# a^2 + ((5/3) * c)^2 = c^2
# a^2 + (25/9) * c^2 = c^2
# a^2 = c^2 - (25/9) * c^2
# a^2 = (9/9) * c^2 - (25/9) * c^2
# a^2 = (-16/9) * c^2
# c^2 = (9/16) * a^2
# c = a * (3/4)

c = a * Fraction(3, 4)  # Distance B walks east in bu
b = c * Fraction(5, 3)  # Distance A walks diagonally northeast in bu

# Final results
a = a  # Distance A walks south to the gate
b = b  # Distance A walks diagonally northeast
c = c  # Distance B walks east

a, b, c  # Output results
"""
Variable 'a' has wrong value. Expected: 800, Actual: 1500
Variable 'b' has wrong value. Expected: 9775/2, Actual: 1875
Variable 'c' has wrong value. Expected: 8625/2, Actual: 1125"""

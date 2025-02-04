"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
Suppose there is a square city with sides of 10 li, and gates are opened at the middle of each side.
Person A and Person B both start from the center of the city. Person B exits through the east gate, while Person A exits through the south gate. After exiting, Person A walks diagonally toward the northeast corner of the city and meets Person B. The ratio of their speeds is such that A walks 5 steps for every 3 steps of B.

Question: How far does Person A walk south to exit the city, how far does Person A walk diagonally, and how far does Person B walk east?

Answer: Person A walks *a* bu south, *b* bu diagonally northeast, and Person B walks *c* bu east.
"""

from fractions import Fraction

# The side length of the city in li
side_length = 10  # li

# Convert li to bu (1 li = 300 bu)
side_length_bu = side_length * 300

# Ratio of speeds: A walks 5 steps for every 3 steps of B
ratio_A_to_B = Fraction(5, 3)

# Let the distance B walks east be c (in bu)
c = Fraction(side_length_bu, 2)  # B walks from the center to the east gate

# Since A and B meet at the same point, the diagonal distance A walks northeast (b) and the distance B walks east (c) form a right triangle.
# The southward distance A walks to exit the city is a = side_length_bu / 2 (from the center to the south gate).

a = Fraction(side_length_bu, 2)  # A's southward distance

# Using the Pythagorean theorem: b^2 = a^2 + c^2
b = (a**2 + c**2).sqrt()

# A's total diagonal distance northeast is scaled by the speed ratio
b = b * ratio_A_to_B.denominator / ratio_A_to_B.numerator

# Output the results
a, b, c
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

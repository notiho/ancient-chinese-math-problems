"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li, and gates are located at the center of each side.
Person A and Person B both start from the center of the city and leave through different gates. Person B exits through the east gate, while Person A exits through the south gate. After exiting, Person A walks diagonally northeast along the city boundary and meets Person B at some point. The walking rates are such that Person A walks 5 steps for every 3 steps Person B walks.

Question: How far does Person A walk south to the gate, how far does Person A walk diagonally northeast, and how far does Person B walk east?

Answer: Person A walks *a* steps south, *b* steps diagonally northeast, and Person B walks *c* steps east.
"""

from fractions import Fraction

# Define the side length of the city in li
side_length = 10  # in li

# Define the walking rates
rate_A = 5  # Person A walks 5 steps
rate_B = 3  # Person B walks 3 steps

# Let the distances walked by Person A and Person B be proportional to their rates
# Let x be the scaling factor for the rates
# Person A's diagonal distance = 5x
# Person B's eastward distance = 3x

# The diagonal distance of Person A forms the hypotenuse of a right triangle
# The two legs of the triangle are:
# 1. The distance Person A walks south to the gate (a)
# 2. The distance Person B walks east (c)

# Using the Pythagorean theorem:
# (5x)^2 = a^2 + (3x)^2

# The side length of the city is 10 li, so:
a = side_length  # Person A walks 10 li south to the gate

# Substitute a = 10 into the Pythagorean theorem:
# (5x)^2 = 10^2 + (3x)^2
# 25x^2 = 100 + 9x^2
# 25x^2 - 9x^2 = 100
# 16x^2 = 100
# x^2 = 100 / 16
# x = sqrt(100 / 16) = 10 / 4 = 5 / 2

x = Fraction(5, 2)

# Calculate the diagonal distance Person A walks (b)
b = 5 * x  # 5x

# Calculate the eastward distance Person B walks (c)
c = 3 * x  # 3x

# Final results
a = side_length  # Person A walks 10 li south to the gate
b = 5 * x  # Person A walks diagonally northeast
c = 3 * x  # Person B walks east

a, b, c  # Output the results as fractions#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 10
Variable 'b' has wrong value. Expected: 9775/2, Actual: 25/2
Variable 'c' has wrong value. Expected: 8625/2, Actual: 15/2"""

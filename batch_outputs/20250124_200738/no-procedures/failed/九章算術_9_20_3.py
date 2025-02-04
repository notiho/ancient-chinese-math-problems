"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with each side 10 li, and gates are opened in the middle of each side. 
Person A and Person B both start from the center of the city. 
Person B exits through the east gate, while Person A exits through the south gate. 
The number of steps they take after exiting is unknown. 
Person A then moves diagonally northeast along the city boundary and meets Person B. 
The ratio of their walking speeds is such that Person A walks 5 steps for every 3 steps Person B walks.

Question: How far does Person A walk south to exit the south gate, how far does Person A walk diagonally northeast, and how far does Person B walk east?

Answer: Person A walks *a* steps south, *b* steps diagonally northeast, and Person B walks *c* steps east.
"""

from fractions import Fraction

# Dimensions of the city
city_side = 10  # li

# Speed ratio of A to B
ratio_A_to_B = Fraction(5, 3)

# Let the distance Person B walks east be c (in li)
c = Fraction(city_side, 2)  # Since Person B exits through the east gate, they walk half the city's side length to the gate.

# Let the diagonal distance Person A walks northeast be b (in li)
# Using the Pythagorean theorem:
# b^2 = (a^2 + c^2), where a is the distance Person A walks south to exit the south gate.
# Also, the time taken by both is the same, so:
# b / 5 = c / 3  (distance divided by speed is time)

# Solve for b in terms of c:
b = (5 / 3) * c

# Solve for a using the Pythagorean theorem:
# b^2 = a^2 + c^2
a = (b**2 - c**2).sqrt()

# Convert results to fractions
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)

# Final results
a_steps = a
b_steps = b
c_steps = c

a_steps, b_steps, c_steps#----- content ends here -----

"""
Code error: 'float' object has no attribute 'sqrt'"""

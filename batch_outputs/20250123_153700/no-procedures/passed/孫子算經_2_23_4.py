"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
Suppose there are five ranks of nobles: Gong (Duke), Hou (Marquis), Bo (Earl), Zi (Viscount), and Nan (Baron).
They are dividing 60 oranges such that each rank receives 3 more oranges than the rank below it.

Question: How many oranges does each rank receive?

Answer: The Duke (Gong) gets *a* oranges, the Marquis (Hou) gets *b* oranges, the Earl (Bo) gets *c* oranges, the Viscount (Zi) gets *d* oranges, and the Baron (Nan) gets *e* oranges.
"""

# Total number of oranges
total_oranges = 60

# Let the number of oranges the Baron (lowest rank) receives be x
# Each rank above receives 3 more oranges than the rank below it:
# Nan = x, Zi = x + 3, Bo = x + 6, Hou = x + 9, Gong = x + 12

# The total number of oranges is the sum of all these:
# x + (x + 3) + (x + 6) + (x + 9) + (x + 12) = 60
# 5x + 30 = 60
# 5x = 30
# x = 6

# Calculate the number of oranges each rank receives
e = 6  # Nan (Baron)
d = e + 3  # Zi (Viscount)
c = d + 3  # Bo (Earl)
b = c + 3  # Hou (Marquis)
a = b + 3  # Gong (Duke)

# Results
a, b, c, d, e  # (12, 9, 6, 3, 6)
"""
"""

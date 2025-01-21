"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
Suppose there are five ranks of nobles: Gong (Duke), Hou (Marquis), Bo (Earl), Zi (Viscount), and Nan (Baron). 
They are to divide 60 oranges such that each rank gets 3 more oranges than the rank below it.
Question: how many oranges does each rank get?

Answer: Gong gets *a* oranges, Hou gets *b* oranges, Bo gets *c* oranges, Zi gets *d* oranges, and Nan gets *e* oranges.
"""

# Total oranges
total_oranges = 60

# Let the number of oranges the lowest rank (Nan) gets be x
# Each rank gets 3 more than the rank below it:
# Nan = x
# Zi = x + 3
# Bo = x + 6
# Hou = x + 9
# Gong = x + 12

# Total oranges equation:
# x + (x + 3) + (x + 6) + (x + 9) + (x + 12) = 60
# 5x + 30 = 60
# 5x = 30
# x = 6

# Calculate the number of oranges for each rank
e = 6  # Nan
d = e + 3  # Zi
c = d + 3  # Bo
b = c + 3  # Hou
a = b + 3  # Gong

# Final results
a, b, c, d, e  # Gong, Hou, Bo, Zi, Nan
"""
"""

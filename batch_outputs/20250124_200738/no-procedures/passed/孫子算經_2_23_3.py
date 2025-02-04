"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of nobles: Gong (Duke), Hou (Marquis), Bo (Earl), Zi (Viscount), and Nan (Baron). Together, they divide 60 oranges, with each rank receiving 3 more than the next lower rank.
Question: how many oranges does each rank receive?

Answer: Gong gets *a* oranges, Hou gets *b* oranges, Bo gets *c* oranges, Zi gets *d* oranges, and Nan gets *e* oranges.
"""

# Total oranges
total_oranges = 60

# Let the number of oranges received by Nan (the lowest rank) be x
# Then Zi gets x + 3, Bo gets x + 6, Hou gets x + 9, and Gong gets x + 12
# The total is: x + (x + 3) + (x + 6) + (x + 9) + (x + 12) = 60

# Solve for x
x = (total_oranges - (3 + 6 + 9 + 12)) // 5

# Calculate the number of oranges for each rank
e = x  # Nan
d = x + 3  # Zi
c = x + 6  # Bo
b = x + 9  # Hou
a = x + 12  # Gong

# Results
a, b, c, d, e#----- content ends here -----

"""
"""

"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of nobles: Gong (Duke), Hou (Marquis), Bo (Earl), Zi (Viscount), and Nan (Baron). 
They are to divide 60 oranges such that each rank gets 3 more oranges than the rank below it.
Question: how many oranges does each rank get?

Answer: The Duke (Gong) gets *a* oranges, the Marquis (Hou) gets *b* oranges, the Earl (Bo) gets *c* oranges, the Viscount (Zi) gets *d* oranges, and the Baron (Nan) gets *e* oranges.
"""

# Total oranges
total_oranges = 60

# Let the Baron (Nan) get x oranges
e = Fraction(total_oranges - 3 * (4 + 3 + 2 + 1), 5)

# Calculate the oranges for each rank
d = e + 3  # Viscount (Zi)
c = d + 3  # Earl (Bo)
b = c + 3  # Marquis (Hou)
a = b + 3  # Duke (Gong)

# Results
a, b, c, d, e#----- content ends here -----

"""
"""

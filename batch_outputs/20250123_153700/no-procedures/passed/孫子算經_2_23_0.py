"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
Suppose there are five ranks of feudal lords: Gong (公), Hou (侯), Bo (伯), Zi (子), and Nan (男).
They are to divide 60 oranges such that each rank receives 3 more oranges than the rank below it.

Question: How many oranges does each rank receive?

Answer: Gong gets *a* oranges, Hou gets *b* oranges, Bo gets *c* oranges, Zi gets *d* oranges, and Nan gets *e* oranges.
"""

# Total oranges
total_oranges = 60

# Let the number of oranges received by Nan (男) be x
# Then Zi (子) gets x + 3, Bo (伯) gets x + 6, Hou (侯) gets x + 9, and Gong (公) gets x + 12
# The total is: x + (x + 3) + (x + 6) + (x + 9) + (x + 12) = 60

# Solve for x
x = (total_oranges - (3 + 6 + 9 + 12)) // 5

# Calculate the number of oranges for each rank
e = x  # Nan (男)
d = x + 3  # Zi (子)
c = x + 6  # Bo (伯)
b = x + 9  # Hou (侯)
a = x + 12  # Gong (公)

# Results
a, b, c, d, e  # 公, 侯, 伯, 子, 男
"""
"""

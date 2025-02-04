"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
答曰：雉 a ，兔 b 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. The total number of heads is 35, and the total number of legs is 94.
Question: how many pheasants and rabbits are there?

Answer: there are *a* pheasants and *b* rabbits.
"""

# Total heads
heads = 35

# Total legs
legs = 94

# Let pheasants = a, rabbits = b
# Each pheasant has 1 head and 2 legs
# Each rabbit has 1 head and 4 legs
# We have the following equations:
# a + b = 35  (total heads)
# 2a + 4b = 94 (total legs)

# Solve for a and b
# From the first equation: b = 35 - a
# Substitute into the second equation:
# 2a + 4(35 - a) = 94
# 2a + 140 - 4a = 94
# -2a = -46
# a = 23

a = 23  # Number of pheasants
b = heads - a  # Number of rabbits
b = 35 - 23#----- content ends here -----

"""
"""

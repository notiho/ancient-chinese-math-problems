"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
答曰：雉 a ，兔 b 。
"""

#----- content starts here -----
"""
Suppose there are pheasants (雉) and rabbits (兔) in the same cage. 
There are 35 heads in total and 94 feet in total.
Question: how many pheasants and rabbits are there?

Answer: there are *a* pheasants and *b* rabbits.
"""

# Total heads
heads = 35

# Total feet
feet = 94

# Let:
# pheasants = a (each has 2 feet)
# rabbits = b (each has 4 feet)

# Solve the system of equations:
# a + b = 35  (total heads)
# 2a + 4b = 94 (total feet)

# From the first equation: b = 35 - a
# Substitute into the second equation:
# 2a + 4(35 - a) = 94
# 2a + 140 - 4a = 94
# -2a = -46
# a = 23

# Solve for b:
# b = 35 - a
# b = 35 - 23
# b = 12

# Final answer:
a = 23  # pheasants
b = 12  # rabbits#----- content ends here -----

"""
"""

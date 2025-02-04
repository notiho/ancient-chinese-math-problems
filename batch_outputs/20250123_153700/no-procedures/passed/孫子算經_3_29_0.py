"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
答曰：雉 a ，兔 b 。
"""

"""
Suppose there are pheasants (雉) and rabbits (兔) in the same cage. 
The total number of heads is 35, and the total number of feet is 94.
Question: how many pheasants and rabbits are there?

Answer: there are *a* pheasants and *b* rabbits.
"""

# Total heads
heads = 35

# Total feet
feet = 94

# Let:
# a = number of pheasants (雉), each with 1 head and 2 feet
# b = number of rabbits (兔), each with 1 head and 4 feet

# Solve the system of equations:
# a + b = heads
# 2a + 4b = feet

# From the first equation: b = heads - a
# Substitute into the second equation:
# 2a + 4(heads - a) = feet
# 2a + 4heads - 4a = feet
# -2a = feet - 4heads
# a = (4heads - feet) / 2

a = (4 * heads - feet) // 2
b = heads - a

# Results
a, b  # a = number of pheasants, b = number of rabbits
"""
"""

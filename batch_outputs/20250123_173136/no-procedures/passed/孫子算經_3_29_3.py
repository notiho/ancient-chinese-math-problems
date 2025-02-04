"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
答曰：雉 a ，兔 b 。
"""

"""
Suppose there are pheasants and rabbits in the same cage. The total number of heads is 35, and the total number of feet is 94.
Question: how many pheasants and rabbits are there?

Answer: There are *a* pheasants and *b* rabbits.
"""

# Total heads
heads = 35

# Total feet
feet = 94

# Let pheasants = a, rabbits = b
# Each pheasant has 1 head and 2 feet
# Each rabbit has 1 head and 4 feet
# We solve the system of equations:
# a + b = 35  (total heads)
# 2a + 4b = 94 (total feet)

# From the first equation, b = 35 - a
# Substitute into the second equation:
# 2a + 4(35 - a) = 94
# 2a + 140 - 4a = 94
# -2a = -46
# a = 23

# Substitute a = 23 into b = 35 - a:
# b = 35 - 23 = 12

a = 23  # Number of pheasants
b = 12  # Number of rabbits
"""
"""

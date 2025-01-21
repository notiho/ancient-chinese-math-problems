"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
答曰：雉 a ，兔 b 。
"""

"""
Suppose there are pheasants and rabbits in the same cage. The total number of heads is 35, and the total number of feet is 94.
Question: how many pheasants and rabbits are there?

Answer: there are *a* pheasants and *b* rabbits.
"""

# Total number of heads
heads = 35

# Total number of feet
feet = 94

# Let the number of pheasants be `a` and the number of rabbits be `b`.
# Pheasants have 2 feet, and rabbits have 4 feet.
# We have the following system of equations:
# a + b = 35  (1)
# 2a + 4b = 94  (2)

# From (1), we can express b in terms of a:
# b = 35 - a

# Substitute b into (2):
# 2a + 4(35 - a) = 94
# 2a + 140 - 4a = 94
# -2a + 140 = 94
# -2a = 94 - 140
# -2a = -46
# a = 23

# Substitute a = 23 into (1):
# 23 + b = 35
# b = 35 - 23
# b = 12

# Final result:
a = 23  # Number of pheasants
b = 12  # Number of rabbits

# Output the result
a, b
"""
"""

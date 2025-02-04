"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads in total and 94 feet in total.
Question: how many pheasants and rabbits are there?

The procedure says: Place the 35 heads above and the 94 feet below. 
Halve the feet, obtaining 47. 
Subtract the smaller number from the larger number, and divide repeatedly:
- Divide the heads by 3 for pheasants.
- Divide the heads by 5 for rabbits.
- Use the remaining feet to adjust the counts.

Answer: there are *a* pheasants and *b* rabbits.
"""

# 上有三十五頭
heads = 35

# 下有九十四足
feet = 94

# 每隻雉有2足，每隻兔有4足
# Let x = number of pheasants, y = number of rabbits
# x + y = heads
# 2x + 4y = feet

# Solve the system of equations:
# From x + y = heads, we get y = heads - x
# Substitute into 2x + 4y = feet:
# 2x + 4(heads - x) = feet
# 2x + 4heads - 4x = feet
# -2x + 4heads = feet
# 2x = 4heads - feet
# x = (4heads - feet) / 2
x = (4 * heads - feet) // 2

# y = heads - x
y = heads - x

# Answer
a = x  # Number of pheasants
b = y  # Number of rabbits

a, b  # Output the result#----- content ends here -----

"""
"""

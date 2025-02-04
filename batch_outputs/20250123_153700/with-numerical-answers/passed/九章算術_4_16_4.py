"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a(=135)步 。
"""

"""
Suppose there is an area of 1518 bu and 3/4 of a bu.
Question: what is the circumference of the circle?

The procedure for opening a circle says: Place the number of bu in the area.
Multiply it by 12.
Extract the square root and divide by it, obtaining the circumference.

Answer: *a*(=135) bu.
"""

from fractions import Fraction

# 積一千五百一十八步、四分步之三
積步數 = 1518 + Fraction(3, 4)

# 以十二乘之
積乘十二 = 12 * 積步數

# 以開方除之，即得周
# 開方 (square root) is approximated manually since no external functions are allowed.
# We find the largest integer n such that n^2 <= 積乘十二.
n = 0
while (n + 1) ** 2 <= 積乘十二:
    n += 1

a = n  # 135
"""
"""

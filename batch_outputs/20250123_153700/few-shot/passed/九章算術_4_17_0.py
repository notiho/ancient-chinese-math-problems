"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""
Suppose there is an area of 300 bu.
Question: what is the circumference of the circle?

The procedure for opening the circle says: Place the area in bu.
Multiply it by 12.
Take the square root of the result, and this gives the circumference.

Answer: *a* bu.
"""

# 積三百步
積步數 = 300

# 以十二乘之
積乘十二 = 12 * 積步數

# 開方 (square root)
# Since Python does not have a built-in square root function, we will use exponentiation to calculate it.
a = Fraction(int(積乘十二**0.5))  # Result is the square root of 積乘十二
"""
"""

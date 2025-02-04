"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a(=135)步 。
"""

"""
Suppose there is an area of 1518 bu and 3/4 of a bu. 
Question: what is the circumference of the circle?

The procedure for opening a circle says: Place the total area in bu, multiply it by 12, and divide it by the square root. This gives the circumference.

Answer: *a*(=135) bu.
"""

from fractions import Fraction

# 積一千五百一十八步、四分步之三
積步數 = 1518 + Fraction(3, 4)

# 置積步數，以十二乘之
積乘十二 = 12 * 積步數

# 開方 (square root approximation via iterative method)
def 開方(x):
    guess = x / 2
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

# 以開方除之，即得周
a = Fraction(積乘十二, 開方(積步數))  # 135
"""
Timed out"""

"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a(=135)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 1518 bu and 3/4 of a bu. 
Question: what is the circumference of the circle?

The procedure for opening a circle says: Place the number of bu in the area.
Multiply it by 12.
Extract the square root and divide, obtaining the circumference.

The answer says: *a*(=135) bu.
"""

from fractions import Fraction

# 積一千五百一十八步、四分步之三
積步數 = 1518 + Fraction(3, 4)

# 以十二乘之
積乘十二 = 12 * 積步數

# 開方 (square root approximation using iterative method)
def 開方(n):
    x = n
    while True:
        y = (x + n / x) / 2
        if abs(x - y) < Fraction(1, 1000000):  # Precision threshold
            return y
        x = y

# 以開方除之，即得周
a = 開方(積乘十二) # 135#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 135, Actual: Too large to be printed"""

"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 1518 bu and 3/4 of a bu.
Question: what is the circumference of the circle?

The procedure for opening a circle says: Place the number of bu in the area.
Multiply it by 12.
Extract the square root and divide by it, obtaining the circumference.

Answer: *a* bu.
"""

from fractions import Fraction

# 積一千五百一十八步、四分步之三
積步數 = 1518 + Fraction(3, 4)

# 以十二乘之
積乘十二 = 12 * 積步數

# 開方 (square root)
# Since we cannot use external libraries, we approximate the square root manually.
def 開方(x):
    # Use a simple iterative method to approximate the square root
    guess = x / 2
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

# 以開方除之，即得周
a = 開方(積乘十二)#----- content ends here -----

"""
Timed out"""

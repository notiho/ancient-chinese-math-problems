"""
今有積一千五百一十八步四分步之三問為圓周幾何
開圓術曰置積步數以十二乘之以開方除之即得周
荅曰 a步 
"""

"""
Suppose there is an area of 1518 and 3/4 bu². 
Question: what is the circumference of the circle?

The procedure for finding the circumference of a circle says: 
Take the area (in bu²) and multiply it by 12. 
Then take the square root of the result, and divide it by 1. 
This gives the circumference.

Answer: *a* bu.
"""

from fractions import Fraction

# 積一千五百一十八步四分步之三
積步數 = 1518 + Fraction(3, 4)

# 置積步數以十二乘之
積乘十二 = 積步數 * 12

# 以開方除之即得周
# Since we cannot directly compute square roots without external libraries, 
# we will represent the square root as a fractional exponent (1/2).
a = 積乘十二 ** Fraction(1, 2)  # This represents the square root of 積乘十二
"""
"""

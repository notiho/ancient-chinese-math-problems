"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 1518 bu and 3/4 of a bu. 
Question: what is the circumference of the circle?

The procedure for circles says: Place the area in bu, multiply it by 12, and then take the square root of the result. This gives the circumference.

Answer: *a* bu.
"""

from fractions import Fraction
import math

# 積一千五百一十八步、四分步之三
積 = 1518 + Fraction(3, 4)

# 以十二乘之
積乘十二 = 12 * 積

# 以開方除之，即得周
a = math.sqrt(積乘十二)

a#----- content ends here -----

"""
"""

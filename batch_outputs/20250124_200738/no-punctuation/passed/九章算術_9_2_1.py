"""
今有股四尺弦五尺問為句幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says:
1. Multiply the ju and gu by themselves, add them together, and take the square root. Divide by this, obtaining the hypotenuse.
2. Multiply the gu by itself, subtract the square of the hypotenuse, and take the square root. Divide by this, obtaining the ju.
3. Multiply the ju by itself, subtract the square of the hypotenuse, and take the square root. Divide by this, obtaining the gu.

Answer: the other leg (ju) is *a* chi.
"""

from fractions import Fraction
import math

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘以減弦自乘
差 = 弦**2 - 股**2

# 其餘開方除之即句
a = math.sqrt(差)  # Taking the square root to find the ju (句)

a = Fraction(a).limit_denominator()  # Representing the result as a fraction#----- content ends here -----

"""
"""

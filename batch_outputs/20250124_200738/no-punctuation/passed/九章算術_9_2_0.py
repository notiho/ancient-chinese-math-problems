"""
今有股四尺弦五尺問為句幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says: Multiply each of the legs (ju and gu) by itself, add them together, and take the square root. Divide by this, and it is the hypotenuse.
Alternatively, multiply the gu by itself, subtract the square of the hypotenuse, and take the square root. Divide by this, and it is the ju.
Alternatively, multiply the ju by itself, subtract the square of the hypotenuse, and take the square root. Divide by this, and it is the gu.

Answer: *a* chi.
"""

from fractions import Fraction
import math

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘以減弦自乘
差 = 弦**2 - 股**2

# 其餘開方除之，即句
a = math.sqrt(差)
#----- content ends here -----

"""
"""

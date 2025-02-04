"""
今有股四尺弦五尺問為句幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says: 
1. Multiply the ju and gu by themselves, add them, and take the square root. Divide by this to get the hypotenuse.
2. Multiply the gu by itself, subtract the square of the hypotenuse, and take the square root. Divide by this to get the ju.
3. Multiply the ju by itself, subtract the square of the hypotenuse, and take the square root. Divide by this to get the gu.

Answer: *a* chi.
"""

from fractions import Fraction
from math import sqrt

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘以減弦自乘
差 = 弦**2 - 股**2

# 其餘開方除之，即句
a = sqrt(差)

"""
"""

"""
今有股四尺弦五尺問為句幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

"""
Suppose there is a right triangle where the leg (gu) is 4 chi and the hypotenuse (xian) is 5 chi.
Question: how long is the other leg (ju)?

The procedure for the legs and hypotenuse says:
- Multiply each of the legs (ju and gu) by itself, add them together, and take the square root. Divide by this to obtain the hypotenuse.
- Multiply the leg (gu) by itself, subtract the square of the hypotenuse, and take the square root. Divide by this to obtain the other leg (ju).
- Multiply the leg (ju) by itself, subtract the square of the hypotenuse, and take the square root. Divide by this to obtain the other leg (gu).

Answer: *a* chi.
"""

from fractions import Fraction

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘以減弦自乘
差 = 弦**2 - 股**2

# 其餘開方除之即句
a = Fraction(差**0.5)  # Taking the square root of the difference
"""
"""

"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says: Multiply the ju and gu by themselves, add them, and take the square root, obtaining the hypotenuse.
Also, multiply the gu by itself, subtract it from the hypotenuse squared, and take the square root, obtaining the ju.
Also, multiply the ju by itself, subtract it from the hypotenuse squared, and take the square root, obtaining the gu.

Answer: *a* chi.
"""

from fractions import Fraction
import math

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘
股平方 = 股 * 股

# 弦自乘
弦平方 = 弦 * 弦

# 以減弦自乘，其餘開方除之，即句
句平方 = 弦平方 - 股平方
句 = math.sqrt(句平方)

a = 句#----- content ends here -----

"""
"""

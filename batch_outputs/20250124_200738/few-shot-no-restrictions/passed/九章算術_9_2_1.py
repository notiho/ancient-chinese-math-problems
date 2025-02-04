"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says:
- Multiply each of the legs (ju and gu) by itself, add them together, and take the square root to obtain the hypotenuse.
- Alternatively, multiply the gu by itself, subtract the square of the hypotenuse, and take the square root to obtain the ju.
- Similarly, multiply the ju by itself, subtract the square of the hypotenuse, and take the square root to obtain the gu.

Answer: *a* chi.
"""

import math

# 股 (gu) = 4 尺
股 = 4

# 弦 (xian) = 5 尺
弦 = 5

# 股自乘，以減弦自乘，其餘開方除之，即句
句平方 = 弦**2 - 股**2
句 = math.sqrt(句平方)

a = 句  # The length of the other leg (ju) in chi#----- content ends here -----

"""
"""

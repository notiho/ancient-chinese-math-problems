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
- Multiply the gu and ju by themselves (square them), add them together, and take the square root to obtain the xian.
- Alternatively, square the gu, subtract the square of the xian, and take the square root to obtain the ju.
- Similarly, square the ju, subtract the square of the xian, and take the square root to obtain the gu.

Answer: *a* chi.
"""

from math import sqrt

# 股 (gu) = 4 尺
股 = 4

# 弦 (xian) = 5 尺
弦 = 5

# 股自乘，以減弦自乘，其餘開方除之，即句
句 = sqrt(弦**2 - 股**2)

# Answer
a = 句
a#----- content ends here -----

"""
"""

"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure says:
- For a right triangle, the square of the two legs (ju and gu) are added together, and the square root of the sum gives the hypotenuse.
- To find one leg (ju), take the square of the hypotenuse (xian), subtract the square of the other leg (gu), and take the square root of the result.
- Similarly, to find the other leg (gu), take the square of the hypotenuse (xian), subtract the square of the first leg (ju), and take the square root of the result.

Answer: *a* chi.
"""

from math import sqrt

# 股 (gu) = 4 尺
股 = 4

# 弦 (xian) = 5 尺
弦 = 5

# 求句 (ju): 弦自乘減股自乘，其餘開方除之
句 = sqrt(弦**2 - 股**2)

a = 句  # Answer in chi
#----- content ends here -----

"""
"""

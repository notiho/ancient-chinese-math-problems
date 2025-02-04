"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a(=4)尺 。
"""

#----- content starts here -----
"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure for right triangles says: 
The two legs (句 and 股) are each multiplied by themselves, summed, and then the square root is taken, giving the hypotenuse (弦).
Alternatively, one leg (股 or 句) is squared, subtracted from the square of the hypotenuse (弦), and the square root of the remainder is taken, giving the other leg.

Answer: *a*(=4) chi.
"""

from fractions import Fraction

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句自乘
句平方 = 句 * 句

# 弦自乘
弦平方 = 弦 * 弦

# 以減弦自乘，其餘開方除之，即股
股平方 = 弦平方 - 句平方

# 開方除之，即股
a = 股平方**(1/2) # 4#----- content ends here -----

"""
"""

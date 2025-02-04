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
1. Multiply each leg (句 and 股) by itself, add them together, and take the square root to obtain the hypotenuse (弦).
2. Multiply the other leg (股) by itself, subtract the square of the hypotenuse (弦), and take the square root to obtain the first leg (句).
3. Multiply the first leg (句) by itself, subtract the square of the hypotenuse (弦), and take the square root to obtain the other leg (股).

The answer says: *a*(=4) chi.
"""

from fractions import Fraction
import math

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句自乘
句平方 = 句 * 句

# 弦自乘
弦平方 = 弦 * 弦

# 句自乘，以減弦自乘，其餘開方除之，即股
股平方 = 弦平方 - 句平方
a = math.sqrt(股平方) # 4#----- content ends here -----

"""
"""

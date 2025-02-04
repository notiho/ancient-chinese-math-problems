"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction
import math

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句股術曰：句股各自乘，并，而開方除之，即弦。
# This step is used to verify the given values of 弦 and 句, but we proceed to calculate 股.

# 又句自乘，以減弦自乘，其餘開方除之，即股。
句平方 = 句 ** 2
弦平方 = 弦 ** 2
股平方 = 弦平方 - 句平方

# 開方除之，即股
a = Fraction(math.isqrt(股平方))

# Answer: 股 a 尺
#----- content ends here -----


"""

"""


"""
"""

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

# 句自乘
句自乘 = 句 ** 2

# 弦自乘
弦自乘 = 弦 ** 2

# 句自乘，以減弦自乘，其餘開方除之，即股
股自乘 = 弦自乘 - 句自乘
股 = math.sqrt(股自乘)

a = 股
#----- content ends here -----


"""

"""


"""
"""

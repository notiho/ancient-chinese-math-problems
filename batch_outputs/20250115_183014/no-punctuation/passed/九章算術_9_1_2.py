"""
今有弦五尺句三尺問為股幾何
句股術曰句股各自乘并而開方除之即弦又股自乘以減弦自乘其餘開方除之即句又句自乘以減弦自乘其餘開方除之即股
荅曰 a尺 
"""

"""
Suppose there is a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

The procedure for the legs and hypotenuse says:
Each leg (句 and 股) is multiplied by itself, their results are added, and the square root is taken. Dividing by this gives the hypotenuse (弦).
Alternatively, multiply the other leg (股) by itself and subtract the square of the hypotenuse (弦). The remainder, when the square root is taken, gives the first leg (句).
Similarly, multiply the first leg (句) by itself and subtract the square of the hypotenuse (弦). The remainder, when the square root is taken, gives the other leg (股).

Answer: *a* chi.
"""

from fractions import Fraction
import math

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# 句自乘
句自乘 = 句 * 句

# 弦自乘
弦自乘 = 弦 * 弦

# 句自乘以減弦自乘
餘 = 弦自乘 - 句自乘

# 其餘開方除之，即股
a = math.sqrt(餘)  # 股
"""
"""

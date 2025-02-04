"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
術曰：令徑二尺五寸自乘，以七寸自乘減之，其餘開方除之，即廣。
荅曰： a尺 。
"""

"""

"""


from fractions import Fraction
import math

# 圓材徑二尺五寸
徑 = 2 + Fraction(5, 10)

# 厚七寸
厚 = Fraction(7, 10)

# 令徑二尺五寸自乘
徑平方 = 徑 * 徑

# 以七寸自乘減之
厚平方 = 厚 * 厚
餘 = 徑平方 - 厚平方

# 其餘開方除之，即廣
a = math.sqrt(float(餘))


"""

"""


"""
Variable 'a' has wrong value. Expected: 12/5, Actual: 2.4"""

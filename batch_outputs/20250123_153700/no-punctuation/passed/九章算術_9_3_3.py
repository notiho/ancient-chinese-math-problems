"""
今有圓材徑二尺五寸欲為方版令厚七寸問廣幾何
術曰令徑二尺五寸自乘以七寸自乘減之其餘開方除之即廣
荅曰 a尺 
"""

"""
Suppose there is a cylindrical log with a diameter of 2 chi and 5 cun. It is desired to make square planks with a thickness of 7 cun.
Question: what is the width of the planks?

The procedure says: Take the diameter of 2 chi and 5 cun, square it. Take the thickness of 7 cun, square it, and subtract it from the squared diameter. Take the square root of the remainder and divide it, obtaining the width.

The answer says: *a* chi.
"""

from fractions import Fraction
import math

# 圓材徑二尺五寸
徑 = 2 + Fraction(5, 10)  # 2 chi and 5 cun (1 chi = 10 cun)

# 厚七寸
厚 = Fraction(7, 10)  # 7 cun

# 令徑二尺五寸自乘
徑平方 = 徑 ** 2

# 以七寸自乘
厚平方 = 厚 ** 2

# 減之
餘 = 徑平方 - 厚平方

# 其餘開方
開方餘 = math.sqrt(float(餘))

# 除之即廣
a = Fraction(開方餘).limit_denominator(100)  # Convert back to a fraction for precision

a  # The width in chi
"""
"""

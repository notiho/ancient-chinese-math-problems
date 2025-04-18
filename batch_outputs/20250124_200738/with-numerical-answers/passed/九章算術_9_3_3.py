"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
術曰：令徑二尺五寸自乘，以七寸自乘減之，其餘開方除之，即廣。
荅曰： a(=12/5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi and 5 cun. It is desired to make square planks with a thickness of 7 cun.
Question: how wide are the planks?

The procedure says: Take the diameter of 2 chi and 5 cun, square it. Then take the thickness of 7 cun, square it, and subtract it from the previous result. Take the square root of the remainder and divide it, obtaining the width.

The answer says: *a*(=12/5) chi.
"""

from fractions import Fraction
import math

# 圓材徑二尺五寸
徑 = Fraction(2, 1) + Fraction(5, 10)  # 2 chi 5 cun = 2.5 chi

# 厚七寸
厚 = Fraction(7, 10)  # 7 cun = 0.7 chi

# 令徑二尺五寸自乘
徑平方 = 徑 * 徑

# 以七寸自乘
厚平方 = 厚 * 厚

# 減之
餘 = 徑平方 - 厚平方

# 其餘開方
餘開方 = Fraction(math.isqrt(餘.numerator), math.isqrt(餘.denominator))

# 即廣
a = 餘開方  # 12/5 chi#----- content ends here -----

"""
"""

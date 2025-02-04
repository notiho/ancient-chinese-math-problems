"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""

"""


from fractions import Fraction
from math import isqrt

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六十分之九
弦多句 = Fraction(9, 36)

# 術曰：冪自乘
冪自乘 = 冪 * 冪

# 倍多數而一，為實
倍多數 = 2 * 弦多句
實 = 冪自乘 * (倍多數 + 1)

# 半多數，為廉法，從
廉法 = Fraction(倍多數, 2)

# 開立方除之，即句
句 = (實 / 廉法) ** Fraction(1, 3)

# 以弦多句加之，即弦
弦 = 句 + 弦多句

# 以句除冪，即股
股 = 冪 / 句

# 答曰：句 a ，股 b ，弦 c
a = 句
b = 股
c = 弦


"""

"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.0217241500264881
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.06017218353260372
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.2717241500264881"""

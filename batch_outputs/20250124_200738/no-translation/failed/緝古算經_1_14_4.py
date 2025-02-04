"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六十分之九
弦多句 = Fraction(9, 36)

# 術曰：冪自乘
冪自乘 = 冪 * 冪

# 倍多數而一，為實
實 = 2 * 弦多句 + 1

# 半多數，為廉法，從
廉法 = Fraction(弦多句, 2)

# 開立方除之，即句
句 = pow(冪自乘 / (實 * 廉法), 1/3)

# 以弦多句加之，即弦
弦 = 句 + 弦多句

# 以句除冪，即股
股 = 冪 / 句

# 答
a = 句
b = 股
c = 弦
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.020887764027330755
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.0625815927819396
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.2708877640273308"""

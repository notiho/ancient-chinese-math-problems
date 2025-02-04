"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
Suppose there is a right triangle where the product of the legs (the "ju" and "gu") is 1/765.
The hypotenuse ("xian") is greater than the shorter leg ("ju") by 9/36.
Question: what are the lengths of the three sides?

The procedure says:
- Square the product of the legs (the "mi"), double the excess number, and add 1. This gives the dividend.
- Take half of the excess number as the divisor (the "lianfa").
- Divide the dividend by the cube root of the divisor to obtain the shorter leg ("ju").
- Add the excess to the shorter leg to obtain the hypotenuse ("xian").
- Divide the product of the legs by the shorter leg to obtain the other leg ("gu").

Answer: the shorter leg is *a*, the other leg is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六分之九
多數 = Fraction(9, 36)

# 冪自乘
冪平方 = 冪 * 冪

# 倍多數而一，為實
實 = 2 * 多數 + 1

# 半多數，為廉法
廉法 = 多數 / 2

# 開立方除之，即句
句 = 冪平方 / 廉法

# 以弦多句加之，即弦
弦 = 句 + 多數

# 以句除冪，即股
股 = 冪 / 句

a = 句
b = 股
c = 弦
"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 8/585225
Variable 'b' has wrong value. Expected: 246/5, Actual: 765/8
Variable 'c' has wrong value. Expected: 205/4, Actual: 585257/2340900"""

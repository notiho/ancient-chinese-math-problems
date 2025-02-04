"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

"""
Suppose there is a right triangle where the product of the legs (the "ju" and "gu") is 1/765.
The hypotenuse (the "xian") is greater than the shorter leg (the "ju") by 9/60.
Question: what are the lengths of the three sides?

The procedure says:
1. Square the product of the legs (the "mi").
2. Double the excess (the difference between the hypotenuse and the shorter leg) and add 1, obtaining the dividend.
3. Take half of the excess as the divisor.
4. Divide the dividend by the divisor, then take the cube root, obtaining the shorter leg (the "ju").
5. Add the excess to the shorter leg to obtain the hypotenuse (the "xian").
6. Divide the product of the legs (the "mi") by the shorter leg to obtain the longer leg (the "gu").

Answer: the shorter leg is *a*, the longer leg is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六十分之九
多數 = Fraction(9, 60)

# 冪自乘
冪平方 = 冪 ** 2

# 倍多數而一，為實
實 = 2 * 多數 + 1

# 半多數，為廉法
廉法 = 多數 / 2

# 開立方除之，即句
句 = (實 / 廉法) ** (1 / 3)

# 以弦多句加之，即弦
弦 = 句 + 多數

# 以句除冪，即股
股 = 冪 / 句

a = 句
b = 股
c = 弦
"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 2.5879786922187686
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.0005051005815519133
Variable 'c' has wrong value. Expected: 205/4, Actual: 2.7379786922187686"""

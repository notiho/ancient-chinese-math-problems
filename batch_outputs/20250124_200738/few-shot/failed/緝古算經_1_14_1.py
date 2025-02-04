"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the legs (the "ju" and "gu") is 1/765, and the hypotenuse (the "xian") is greater than the "ju" by 9/36.
Question: what are the lengths of the three sides?

The procedure says:
1. Square the product of the legs (the "mi"), double the excess amount (the "duo shu"), and add 1 to obtain the dividend.
2. Take half of the excess amount as the divisor (the "lian fa").
3. Divide the dividend by the divisor, then take the cube root to obtain the "ju".
4. Add the excess amount to the "ju" to obtain the "xian".
5. Divide the product of the legs (the "mi") by the "ju" to obtain the "gu".

Answer: the "ju" is *a*, the "gu" is *b*, and the "xian" is *c*.
"""

from fractions import Fraction

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六十分之九
多數 = Fraction(9, 36)

# 冪自乘
冪平方 = 冪 * 冪

# 倍多數而一，為實
實 = 2 * 多數 + 1

# 半多數，為廉法
廉法 = 多數 / 2

# 開立方除之，即句
句 = (實 / 廉法) ** Fraction(1, 3)

# 以弦多句加之，即弦
弦 = 句 + 多數

# 以句除冪，即股
股 = 冪 / 句

a = 句
b = 股
c = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 2.2894284851066637
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.0005709676240106529
Variable 'c' has wrong value. Expected: 205/4, Actual: 2.5394284851066637"""

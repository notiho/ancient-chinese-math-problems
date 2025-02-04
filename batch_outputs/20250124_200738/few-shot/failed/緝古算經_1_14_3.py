"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a ，股 b ，弦 c 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (ju) and height (gu) is 1/765.
The hypotenuse (xian) is greater than the base by 9/36.
Question: what are the values of the base (ju), height (gu), and hypotenuse (xian)?

The procedure says:
1. Square the product of the base and height (mi), then double the excess amount (of the hypotenuse over the base) and add 1 to it. This becomes the dividend.
2. Take half of the excess amount as the divisor (lianfa).
3. Divide the dividend by the cube root of the divisor to find the base (ju).
4. Add the excess amount to the base to find the hypotenuse (xian).
5. Divide the product of the base and height (mi) by the base to find the height (gu).

Answer: the base is *a*, the height is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪 (mi) is the product of the base and height
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
c = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 8/585225
Variable 'b' has wrong value. Expected: 246/5, Actual: 765/8
Variable 'c' has wrong value. Expected: 205/4, Actual: 585257/2340900"""

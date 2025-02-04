"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a(=287/20) ，股 b(=246/5) ，弦 c(=205/4) 。
"""

"""
Suppose there is a right triangle where the product of the legs (the "ju" and "gu") equals 1/765.
The hypotenuse ("xian") is greater than the shorter leg ("ju") by 9/36 (or 1/4).
Question: what are the values of the three sides?

The procedure says:
1. Square the product of the legs (the "mi").
2. Double the excess (the difference between the hypotenuse and the shorter leg) and add 1 to it. This becomes the dividend.
3. Half the excess becomes the divisor.
4. Divide the cube root of the dividend by the divisor to find the shorter leg ("ju").
5. Add the excess to the shorter leg to find the hypotenuse ("xian").
6. Divide the product of the legs by the shorter leg to find the longer leg ("gu").

Answer: *a*(=287/20) for the shorter leg ("ju"), *b*(=246/5) for the longer leg ("gu"), and *c*(=205/4) for the hypotenuse ("xian").
"""

from fractions import Fraction

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六分之九
多數 = Fraction(9, 36)  # Simplifies to 1/4

# 冪自乘
冪平方 = 冪 * 冪

# 倍多數而一，為實
實 = 2 * 多數 + 1

# 半多數，為廉法
廉法 = 多數 / 2

# 開立方除之，即句
句 = Fraction(實, 廉法)

# 以弦多句加之，即弦
弦 = 句 + 多數

# 以句除冪，即股
股 = 冪 / 句

a = 句  # 287/20
b = 股  # 246/5
c = 弦  # 205/4
"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 12
Variable 'b' has wrong value. Expected: 246/5, Actual: 1/9180
Variable 'c' has wrong value. Expected: 205/4, Actual: 49/4"""

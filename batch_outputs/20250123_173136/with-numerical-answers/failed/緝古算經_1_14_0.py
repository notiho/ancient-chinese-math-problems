"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a(=287/20) ，股 b(=246/5) ，弦 c(=205/4) 。
"""

"""
Suppose there is a right triangle where the product of the base (ju) and the height (gu) is 1/765 of the square of the hypotenuse (xian).
The hypotenuse exceeds the base by 9/36 (or 1/4).
Question: what are the values of the three sides?

The procedure says:
1. Square the given product (1/765), multiply it by twice the excess (1/4), and add 1. This gives the dividend.
2. Take half of the excess (1/4), which is 1/8, as the divisor.
3. Extract the cube root of the division result to find the base (ju).
4. Add the excess (1/4) to the base to find the hypotenuse (xian).
5. Divide the product (1/765) by the base to find the height (gu).

Answer: the base (ju) is *a*(=287/20), the height (gu) is *b*(=246/5), and the hypotenuse (xian) is *c*(=205/4).
"""

from fractions import Fraction

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六分之九
多數 = Fraction(9, 36)  # Simplifies to 1/4

# 冪自乘
冪平方 = 冪 * 冪

# 倍多數而一，為實
實 = 2 * 多數 * 冪平方 + 1

# 半多數，為廉法，從
廉法 = Fraction(多數, 2)

# 開立方除之，即句
句 = (實 / 廉法) ** Fraction(1, 3)

# 以弦多句加之，即弦
弦 = 句 + 多數

# 以句除冪，即股
股 = 冪 / 句

# Final results
a = 句  # 287/20
b = 股  # 246/5
c = 弦  # 205/4
"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 2.0000005695813377
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.000653594585104191
Variable 'c' has wrong value. Expected: 205/4, Actual: 2.2500005695813377"""

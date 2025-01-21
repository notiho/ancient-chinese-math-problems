"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
術曰：冪自乘，倍多而一，為立冪。又多再自乘，半之，減立冪，余為實。又多數自乘，倍之，為方法。又置多數，五之，二而一，為廉法，從。開立方除之，即股。案：此術脫簡既多，法亦煩擾，宜雲冪自乘，多數而一，所得四之，為實。多為廉法，從。立方開之，得減差，半之，即股。
答曰： a(=462/5) 。
"""

"""
Suppose there is a right triangle where the product of the hypotenuse and the base is 1337 and 1/20. The hypotenuse exceeds the perpendicular by 1 and 1/10.
Question: what is the length of the perpendicular?

The procedure says: Square the product (冪), double the excess (多) and add 1, obtaining the cubic power (立冪). 
Then square the excess again, halve it, and subtract the cubic power, leaving the remainder as the dividend (實). 
Square the excess, double it, obtaining the divisor (方法). 
Also place the excess, multiply it by 5, and divide by 2, obtaining the auxiliary divisor (廉法). 
Extract the cube root and divide by the auxiliary divisor, obtaining the perpendicular.

However, the procedure is simplified: Square the product, divide by the excess plus 1, divide the result by 4, obtaining the dividend. 
The excess is the auxiliary divisor. Extract the cube root, subtract the difference, halve it, obtaining the perpendicular.

Answer: *a*(=462/5).
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一、十分之一
多 = Fraction(1, 1) + Fraction(1, 10)

# 簡化術：
# 冪自乘
冪平方 = 冪 ** 2

# 多數而一
實 = 冪平方 / (多 + 1)

# 所得四之
實 = 實 / 4

# 多為廉法
廉法 = 多

# 立方開之
立方根 = 實 ** Fraction(1, 3)

# 得減差，半之，即股
股 = (立方根 - 多) / 2

a = 股  # 462/5
"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 29.302131167831586"""

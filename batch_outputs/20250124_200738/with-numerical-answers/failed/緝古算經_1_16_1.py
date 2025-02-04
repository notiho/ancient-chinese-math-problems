"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
術曰：冪自乘，倍多而一，為立冪。又多再自乘，半之，減立冪，余為實。又多數自乘，倍之，為方法。又置多數，五之，二而一，為廉法，從。開立方除之，即股。案：此術脫簡既多，法亦煩擾，宜雲冪自乘，多數而一，所得四之，為實。多為廉法，從。立方開之，得減差，半之，即股。
答曰： a(=462/5) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the hypotenuse and the base (the "power") is 1337 and 1/20. The hypotenuse exceeds the perpendicular by 1 and 1/10.
Question: how long is the perpendicular?

The procedure says: Square the power, double the excess, and add 1 to obtain the cubic power. Then square the excess again, divide it by 2, and subtract it from the cubic power to get the remainder. Then square the excess, double it, and use it as the divisor. Multiply the excess by 5, divide it by 2, and use it as the "edge divisor." Divide the cube root of the remainder by this divisor to get the perpendicular.

However, the procedure is overly complicated and simplified as follows: Square the power, divide it by the excess plus 1, and divide the result by 4 to get the remainder. Use the excess as the "edge divisor." Take the cube root of the remainder, subtract the excess, and divide by 2 to get the perpendicular.

Answer: *a*(=462/5).
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一、十分之一
多 = Fraction(1, 1) + Fraction(1, 10)

# 簡化術：冪自乘，多數而一，所得四之，為實
實 = (冪 ** 2) / (多 + 1) / 4

# 多為廉法，從
廉法 = 多

# 立方開之，得減差，半之，即股
股 = (實 ** (1 / 3) - 多) / 2

a = 股 # 462/5#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 29.302131167831586"""

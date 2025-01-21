"""
假令有句弦相乘冪一千三百三十七二十分之一弦多股一十分之一問股多少
術曰冪自乘倍多而一為立冪又多再自乘半之減立冪余為實又多數自乘倍之為方法又置多數五之二而一為廉法從開立方除之即股案此術脫簡既多法亦煩擾宜雲冪自乘多數而一所得四之為實多為廉法從立方開之得減差半之即股
答曰 a 
"""

"""
Suppose there is a right triangle where the product of the base and hypotenuse is 1337 1/20. The hypotenuse exceeds the perpendicular by 1/10.
Question: how long is the perpendicular?

The procedure says: Multiply the product (冪) by itself, double the excess (多) and add 1 to form the cubic power (立冪). Then, multiply the excess again, square it, and halve it. Subtract this from the cubic power to form the dividend (實). Multiply the excess by itself, double it, and use this as the divisor (方法). Place the excess, multiply it by 5, add 2, and use this as the auxiliary divisor (廉法). Extract the cube root of the dividend divided by the divisor, and this gives the perpendicular.

However, this procedure is overly complicated. A simplified method is as follows: Multiply the product (冪) by the excess (多) and add 1. Divide the result by 4 to form the dividend (實). Use the excess (多) as the divisor (廉法). Extract the cube root of the dividend divided by the divisor, subtract the difference, and halve it to obtain the perpendicular.

Answer: *a*.
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一十分之一
多 = Fraction(1, 10)

# 簡化術：冪自乘多數而一所得四之為實
實 = (冪 * 多 + 1) / 4

# 多為廉法
廉法 = 多

# 從立方開之得減差半之即股
a = (實 / 廉法) ** Fraction(1, 3) / 2
"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 3.478654093196541"""

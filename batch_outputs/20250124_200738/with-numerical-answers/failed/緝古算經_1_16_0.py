"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
術曰：冪自乘，倍多而一，為立冪。又多再自乘，半之，減立冪，余為實。又多數自乘，倍之，為方法。又置多數，五之，二而一，為廉法，從。開立方除之，即股。案：此術脫簡既多，法亦煩擾，宜雲冪自乘，多數而一，所得四之，為實。多為廉法，從。立方開之，得減差，半之，即股。
答曰： a(=462/5) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the hypotenuse and the base (the "power") is 1337 and 1/20. 
The hypotenuse exceeds the perpendicular by 1 and 1/10. 
Question: how long is the perpendicular?

The procedure says: Square the power, double the excess, and add 1 to obtain the cubic power. 
Then square the excess again, halve it, and subtract the cubic power to get the remainder. 
Square the excess, double it, and use it as the divisor. 
Also, multiply the excess by 5, divide by 2, and use it as the "edge divisor." 
Extract the cube root and divide by the divisor to get the perpendicular.

However, the procedure is simplified: Square the power, divide by the excess plus 1, and divide the result by 4 to get the remainder. 
Use the excess as the "edge divisor." 
Extract the cube root, subtract the difference, and halve it to get the perpendicular.

Answer: *a*(=462/5).
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一、十分之一
多 = Fraction(1, 1) + Fraction(1, 10)

# 簡化術
# 冪自乘
冪平方 = 冪 ** 2

# 多數而一
實 = 冪平方 / (多 + 1)

# 所得四之
實 = 實 / 4

# 多為廉法，從
廉法 = 多

# 立方開之
立方根 = 實 ** (1 / 3)

# 得減差，半之，即股
a = (立方根 - 多) / 2  # 462/5#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 29.302131167831586"""

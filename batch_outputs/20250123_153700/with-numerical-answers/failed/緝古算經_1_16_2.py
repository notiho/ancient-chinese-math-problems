"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
術曰：冪自乘，倍多而一，為立冪。又多再自乘，半之，減立冪，余為實。又多數自乘，倍之，為方法。又置多數，五之，二而一，為廉法，從。開立方除之，即股。案：此術脫簡既多，法亦煩擾，宜雲冪自乘，多數而一，所得四之，為實。多為廉法，從。立方開之，得減差，半之，即股。
答曰： a(=462/5) 。
"""

"""
Suppose there is a right triangle where the product of the hypotenuse and the base is 1337 1/20 (or 1337.05). 
The hypotenuse exceeds the perpendicular by 1 1/10 (or 1.1). 
Question: what is the length of the perpendicular?

The procedure says: 
1. Square the given product (冪自乘), double the excess (倍多) and add 1, obtaining the cubic power (立冪).
2. Square the excess again (多再自乘), halve it (半之), subtract it from the cubic power (減立冪), and the remainder is the dividend (余為實).
3. Square the excess (多數自乘), double it (倍之), obtaining the divisor (為方法).
4. Multiply the excess by 5, divide by 2, and add 1, obtaining the "edge divisor" (廉法).
5. Divide the cube root of the dividend by the divisor, obtaining the perpendicular.

The simplified procedure says: 
1. Square the product (冪自乘), divide by the excess plus 1 (多數而一), and divide the result by 4, obtaining the dividend (為實).
2. Use the excess as the "edge divisor" (廉法).
3. Take the cube root of the dividend, subtract the divisor, halve the result, and obtain the perpendicular.

Answer: *a*(=462/5).
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一、十分之一
多 = Fraction(1, 1) + Fraction(1, 10)

# 冪自乘
冪平方 = 冪 ** 2

# 多數而一
多數而一 = 多 + 1

# 所得四之，為實
實 = Fraction(冪平方, 多數而一) / 4

# 多為廉法
廉法 = 多

# 立方開之，得減差
減差 = 實 ** Fraction(1, 3) - 廉法

# 半之，即股
a = 減差 / 2  # 462/5
"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 29.302131167831586"""

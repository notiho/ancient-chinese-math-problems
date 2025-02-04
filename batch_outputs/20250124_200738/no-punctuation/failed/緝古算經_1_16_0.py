"""
假令有句弦相乘冪一千三百三十七二十分之一弦多股一十分之一問股多少
術曰冪自乘倍多而一為立冪又多再自乘半之減立冪余為實又多數自乘倍之為方法又置多數五之二而一為廉法從開立方除之即股案此術脫簡既多法亦煩擾宜雲冪自乘多數而一所得四之為實多為廉法從立方開之得減差半之即股
答曰 a 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 1337 1/20. The hypotenuse is longer than the other leg (gu) by 1/10. 
Question: how long is the leg (gu)?

The procedure says: 
1. Multiply the given product (mi) by itself, double the excess (difference between hypotenuse and leg), and add 1. This becomes the cubic power (立冪).
2. Add the excess again, multiply it by itself, and halve it. Subtract this from the cubic power to get the dividend (實).
3. Multiply the excess by itself, double it, and this becomes the divisor (方法).
4. Place the excess, multiply it by 5, add 2, and this becomes the auxiliary divisor (廉法).
5. Extract the cube root of the dividend divided by the divisor, and this gives the leg (gu).

The procedure is complex and redundant. A simplified version is:
1. Multiply the given product (mi) by the excess (difference between hypotenuse and leg) plus 1, divide by 4 to get the dividend (實).
2. The excess becomes the divisor (廉法).
3. Extract the cube root of the dividend divided by the divisor, subtract half the difference, and this gives the leg (gu).

Answer: *a*.
"""

from fractions import Fraction

# 冪 (mi) = 1337 1/20
冪 = Fraction(1337) + Fraction(1, 20)

# 弦多股 (difference between hypotenuse and leg) = 1/10
多數 = Fraction(1, 10)

# 簡化術：
# 冪自乘多數而一所得四之為實
實 = (冪 * (多數 + 1)) / 4

# 多為廉法
廉法 = 多數

# 從立方開之得
股 = (實 / 廉法) ** Fraction(1, 3)

# 減差半之
a = 股 - (多數 / 2)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 15.384531356147404"""

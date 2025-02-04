"""
假令有句弦相乘冪一千三百三十七二十分之一弦多股一十分之一問股多少
術曰冪自乘倍多而一為立冪又多再自乘半之減立冪余為實又多數自乘倍之為方法又置多數五之二而一為廉法從開立方除之即股案此術脫簡既多法亦煩擾宜雲冪自乘多數而一所得四之為實多為廉法從立方開之得減差半之即股
答曰 a 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base and hypotenuse is 1337 and 1/20. 
The hypotenuse exceeds the base by 1/10. 
Question: how long is the base?

The procedure says: 
1. Multiply the product (冪) by itself and double the excess (多) plus 1. This becomes the cubic power (立冪).
2. Add the excess (多) again, multiply it by itself, and halve it. Subtract this from the cubic power to get the dividend (實).
3. Multiply the excess (多) by itself and double it. This becomes the divisor (方法).
4. Place the excess (多), multiply it by 5, and add 2. This becomes the auxiliary divisor (廉法).
5. Extract the cube root of the dividend divided by the divisor. This gives the base.

The procedure is overly complex. A simplified version is:
1. Multiply the product (冪) by the excess (多) plus 1. Divide the result by 4 to get the dividend (實).
2. Use the excess (多) as the divisor (廉法).
3. Extract the cube root of the dividend divided by the divisor. Subtract half the difference to get the base.

Answer: the base is *a*.
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一十分之一
多 = Fraction(1, 10)

# 簡化術：
# 冪自乘多數而一所得四之為實
實 = (冪 * (多 + 1)) / 4

# 多為廉法
廉法 = 多

# 從立方開之得減差半之即股
a = (實 / 廉法) ** (1 / 3) - (多 / 2)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 15.384531356147404"""

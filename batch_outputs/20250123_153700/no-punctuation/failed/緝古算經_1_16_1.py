"""
假令有句弦相乘冪一千三百三十七二十分之一弦多股一十分之一問股多少
術曰冪自乘倍多而一為立冪又多再自乘半之減立冪余為實又多數自乘倍之為方法又置多數五之二而一為廉法從開立方除之即股案此術脫簡既多法亦煩擾宜雲冪自乘多數而一所得四之為實多為廉法從立方開之得減差半之即股
答曰 a 
"""

"""
Suppose there is a right triangle where the product of the base (gu) and the hypotenuse (xian) is 1337 1/20. 
The hypotenuse exceeds the base by 1/10. 
Question: how long is the base (gu)?

The procedure says: 
1. Multiply the given product (mi) by itself, double the excess (duo), and add 1 to form the cubic power (li mi).
2. Add the excess (duo) again, multiply it by itself, and halve it. Subtract this from the cubic power to form the dividend (shi).
3. Multiply the excess (duo) by itself, double it, and use this as the divisor (fang fa).
4. Place the excess (duo), multiply it by 5, and add 2 to form the auxiliary divisor (lian fa).
5. Extract the cube root of the dividend divided by the divisor, and this gives the base (gu).

However, this procedure is overly complex. A simplified version is as follows:
1. Multiply the given product (mi) by the excess (duo) and add 1. Divide the result by 4 to form the dividend (shi).
2. Use the excess (duo) as the divisor (lian fa).
3. Extract the cube root of the dividend divided by the divisor, subtract half the difference, and this gives the base (gu).

Answer: *a*.
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一十分之一
多數 = Fraction(1, 10)

# 簡化術：
# 冪自乘多數而一
實 = 冪 * 多數 + 1

# 所得四之為實
實 = Fraction(實, 4)

# 多為廉法
廉法 = 多數

# 從立方開之
a = (實 / 廉法) ** Fraction(1, 3)
"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 6.957308186393082"""

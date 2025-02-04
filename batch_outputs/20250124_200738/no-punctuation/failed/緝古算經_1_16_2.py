"""
假令有句弦相乘冪一千三百三十七二十分之一弦多股一十分之一問股多少
術曰冪自乘倍多而一為立冪又多再自乘半之減立冪余為實又多數自乘倍之為方法又置多數五之二而一為廉法從開立方除之即股案此術脫簡既多法亦煩擾宜雲冪自乘多數而一所得四之為實多為廉法從立方開之得減差半之即股
答曰 a 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (gu) and the hypotenuse (xian) is 1337 and 1/20. The hypotenuse exceeds the base by 1/10.
Question: how long is the base (gu)?

The procedure says: Multiply the product (mi) by itself, double the excess (duo), and add 1. This becomes the cubic power (li mi).
Then, multiply the excess (duo) again, square it, and halve it. Subtract this from the cubic power to obtain the dividend (shi).
Next, square the excess (duo), double it, and this becomes the divisor (fang fa).
Also, multiply the excess (duo) by 5, add 2, and divide by 1. This becomes the auxiliary divisor (lian fa).
Finally, take the cube root of the dividend, divide it by the divisor, and this gives the base (gu).

However, this procedure is overly complex. A simplified method is as follows:
Multiply the product (mi) by the excess (duo) and add 1. Divide the result by 4 to obtain the dividend (shi).
The excess (duo) becomes the divisor (lian fa).
Take the cube root of the dividend, and this gives the base (gu).

Answer: *a*.
"""

from fractions import Fraction

# 冪一千三百三十七二十分之一
冪 = Fraction(1337, 1) + Fraction(1, 20)

# 弦多股一十分之一
多數 = Fraction(1, 10)

# 簡化術：
# 冪自乘多數而一，所得四之為實
實 = (冪 * 多數 + 1) / 4

# 多為廉法
廉法 = 多數

# 從立方開之，即股
a = 實 ** (1 / 3) / 廉法#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 32.2929639899649"""

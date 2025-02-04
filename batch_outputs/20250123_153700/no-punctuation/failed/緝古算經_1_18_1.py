"""
假令有股弦相乘冪七百二十六句七十分之七問股多少
術曰冪自乘為實句自乘為方法從開方除之所得又開方即股
答曰股 a 
"""

"""
Suppose there is a right triangle where the product of the leg (gu) and hypotenuse (xian) is 726 and the other leg (ju) is 7 7/70 (or 7 + 1/10).
Question: how long is the leg (gu)?

The procedure says: Square the product (mi), obtaining the dividend.
Square the other leg (ju), obtaining the divisor.
Divide the dividend by the divisor, obtaining the result.
Take the square root of the result, and that is the length of the leg (gu).

Answer: the leg (gu) is *a*.
"""

from fractions import Fraction

# 冪七百二十六
冪 = 726

# 句七十分之七
句 = 7 + Fraction(7, 70)

# 冪自乘為實
實 = 冪 ** 2

# 句自乘為方法
方法 = 句 ** 2

# 從開方除之所得
所得 = Fraction(實, 方法)

# 又開方即股
a = 所得 ** Fraction(1, 2)  # Square root of the result
"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 102.25352112676057"""

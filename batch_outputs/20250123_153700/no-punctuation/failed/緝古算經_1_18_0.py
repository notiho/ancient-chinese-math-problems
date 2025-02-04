"""
假令有股弦相乘冪七百二十六句七十分之七問股多少
術曰冪自乘為實句自乘為方法從開方除之所得又開方即股
答曰股 a 
"""

"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 726 7/70, and the other leg (ju) is 7.
Question: how long is the leg (gu)?

The procedure says: Square the product (mi) to obtain the dividend.
Square the other leg (ju) to obtain the divisor.
Divide the dividend by the divisor, and then take the square root of the result to obtain the leg (gu).

Answer: the leg (gu) is *a*.
"""

from fractions import Fraction

# 冪七百二十六句七十分之七
冪 = Fraction(726) + Fraction(7, 70)

# 句七
句 = 7

# 冪自乘為實
實 = 冪 * 冪

# 句自乘為方法
方法 = 句 * 句

# 從開方除之所得
所得 = 實 / 方法

# 又開方即股
a = 所得 ** Fraction(1, 2)  # Square root calculation

a
"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 103.72857142857143"""

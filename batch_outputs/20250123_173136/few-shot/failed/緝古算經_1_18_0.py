"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 726, and the other leg (ju) is 7 and 7/10 (7.7 in decimal form).
Question: how long is the other leg (gu)?

The procedure says: Square the product (mi), obtaining the dividend.
Square the given leg (ju), obtaining the divisor.
Divide the dividend by the divisor, and then take the square root of the result. This gives the length of the other leg (gu).

Answer: the other leg (gu) is *a*.
"""

from fractions import Fraction

# 冪七百二十六
冪 = 726

# 句七、十分之七
句 = 7 + Fraction(7, 10)

# 冪自乘，為實
實 = 冪 ** 2

# 句自乘，為方法
方法 = 句 ** 2

# 從。開方除之，所得又開方，即股
股平方 = Fraction(實, 方法)
a = 股平方 ** Fraction(1, 2)  # 開方 to find 股


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 94.28571428571428"""

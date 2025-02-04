"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and hypotenuse (xian) is 726, and the other leg (ju) is 7 and 7/10 (7.7 in decimal form).
Question: what is the length of the unknown leg (gu)?

The procedure says:
1. Square the product (mi), obtaining the dividend.
2. Square the given leg (ju), obtaining the divisor.
3. Divide the dividend by the divisor, then take the square root of the result to obtain the unknown leg (gu).

Answer: the unknown leg (gu) is *a*.
"""

from fractions import Fraction
import math

# 冪 (mi) is the product of gu and xian
冪 = 726

# 句 (ju) is given as 7 and 7/10
句 = 7 + Fraction(7, 10)

# 冪自乘，為實
實 = 冪 ** 2

# 句自乘，為方法
方法 = 句 ** 2

# 從。開方除之，所得又開方，即股
股 = math.sqrt(實 / 方法)

a = 股
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 94.28571428571428"""

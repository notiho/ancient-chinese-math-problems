"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and hypotenuse (xian) is 726, and the other leg (ju) is 7 and 7/10 (7.7 in decimal form).
Question: how long is the leg (gu)?

The procedure says: 
1. Multiply the product (mi) by itself to get the dividend (shi).
2. Multiply the other leg (ju) by itself to get the divisor (fangfa).
3. Divide the dividend by the divisor, then take the square root of the result to get the leg (gu).

Answer: the leg (gu) is *a*.
"""

from fractions import Fraction
import math

# 冪 (mi) = 股弦相乘 = 726
冪 = 726

# 句 (ju) = 7 + 7/10
句 = 7 + Fraction(7, 10)

# 冪自乘，為實 (shi)
實 = 冪 ** 2

# 句自乘，為方法 (fangfa)
方法 = 句 ** 2

# 從。開方除之，所得又開方，即股
股平方 = 實 / 方法
股 = math.sqrt(股平方)

# 答案
a = 股
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 94.28571428571428"""

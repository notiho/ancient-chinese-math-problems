"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction
import math

# 冪七百二十六
冪 = 726

# 句七、十分之七
句 = 7 + Fraction(7, 10)

# 術曰：冪自乘，為實
實 = 冪 * 冪

# 句自乘，為方法
方法 = 句 * 句

# 從：開方除之
從 = math.sqrt(實 / 方法)

# 所得又開方，即股
a = math.sqrt(從)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 9.710083124552245"""

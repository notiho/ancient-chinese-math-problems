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
實 = 冪

# 句自乘，為方法，從
方法 = 句 * 句

# 開方除之，所得又開方，即股
股平方 = Fraction(實, 方法)
股 = math.sqrt(float(股平方))

a = 股
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 3.499271061118826"""

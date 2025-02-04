"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
術曰：冪自乘，為實。股自乘，為方法，從。開方除之，所得又開方，即句。
答曰：句 a 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction
import math

# 股十六二分之一
股 = 16 + Fraction(1, 2)

# 冪一百六十四二十五分之十四
冪 = 164 + Fraction(14, 25)

# 冪自乘，為實
實 = 冪 * 冪

# 股自乘，為方法
方法 = 股 * 股

# 從。開方除之，所得又開方，即句
句平方 = Fraction(實, 方法)
句 = math.sqrt(float(句平方))

a = 句
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 9.973333333333334"""

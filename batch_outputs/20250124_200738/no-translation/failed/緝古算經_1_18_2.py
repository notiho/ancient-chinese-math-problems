"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 冪七百二十六
冪 = 726

# 句七、十分之七
句 = 7 + Fraction(7, 10)

# 術曰：冪自乘，為實
實 = 冪 * 冪

# 句自乘，為方法
方法 = 句 * 句

# 從：開方除之，所得又開方，即股
# 開方即為平方根，這裡用冪次方的形式表示開方
股 = (實 / 方法) ** Fraction(1, 2)

a = 股
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 94.28571428571428"""

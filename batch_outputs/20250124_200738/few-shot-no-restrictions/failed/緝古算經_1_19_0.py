"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
術曰：冪自乘，為實。股自乘，為方法，從。開方除之，所得又開方，即句。
答曰：句 a 。
"""

#----- content starts here -----
"""
Suppose there is a leg (股) of length 16 1/2, and the product of the other leg (句) and the hypotenuse (弦) is given as 164 14/25.
Question: what is the length of the other leg (句)?

The procedure says: Square the product (冪), obtaining the dividend (實).
Square the given leg (股), obtaining the divisor (方法).
Divide the dividend by the divisor, then take the square root of the result to obtain the length of the other leg (句).

Answer: the length of the other leg (句) is *a*.
"""

from fractions import Fraction
import math

# 股 (leg) = 16 1/2
股 = Fraction(33, 2)

# 冪 (product of 句 and 弦) = 164 14/25
冪 = Fraction(4129, 25)

# 冪自乘，為實
實 = 冪 ** 2

# 股自乘，為方法
方法 = 股 ** 2

# 實除以方法
結果 = 實 / 方法

# 開方，即句
a = math.sqrt(結果)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 10.00969696969697"""

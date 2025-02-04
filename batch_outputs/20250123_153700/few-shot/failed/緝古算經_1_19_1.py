"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
術曰：冪自乘，為實。股自乘，為方法，從。開方除之，所得又開方，即句。
答曰：句 a 。
"""

"""
Suppose there is a leg (股) of 16 1/2, and the product of the other leg (句) and the hypotenuse (弦) is 164 14/25.
Question: how long is the other leg (句)?

The procedure says: Square the product (冪), obtaining the dividend.
Square the given leg (股), obtaining the divisor.
Divide the dividend by the divisor, and then take the square root of the result, obtaining the other leg (句).

Answer: the other leg is *a*.
"""

from fractions import Fraction
import math

# 股十六二分之一
股 = Fraction(33, 2)

# 冪一百六十四二十五分之十四
冪 = Fraction(164 * 25 + 14, 25)

# 冪自乘，為實
實 = 冪 * 冪

# 股自乘，為方法
方法 = 股 * 股

# 從。開方除之，所得又開方，即句
句平方 = 實 / 方法
a = math.sqrt(float(句平方))  # Taking the square root to find 句
"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 9.973333333333334"""

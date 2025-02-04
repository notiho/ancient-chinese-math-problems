"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
術曰：冪自乘，為實。股自乘，為方法，從。開方除之，所得又開方，即句。
答曰：句 a 。
"""

#----- content starts here -----
"""
Suppose there is a leg (股) of 16 1/2 (16.5), and the product of the other leg (句) and the hypotenuse (弦) is 164 14/25 (164.56).
Question: what is the length of the other leg (句)?

The procedure says: Square the product (冪) to obtain the dividend (實).
Square the given leg (股) to obtain the divisor (方法).
Divide the dividend by the divisor, and then take the square root of the result to obtain the other leg (句).

Answer: the other leg (句) is *a*.
"""

from fractions import Fraction
import math

# 股 (leg) = 16 1/2
股 = Fraction(33, 2)

# 冪 (product of 句 and 弦) = 164 14/25
冪 = Fraction(4124, 25)

# 冪自乘，為實
實 = 冪 ** 2

# 股自乘，為方法
方法 = 股 ** 2

# 從。開方除之，所得又開方，即句
句平方 = 實 / 方法
句 = math.sqrt(float(句平方))

a = Fraction(句).limit_denominator(1000)  # Approximate the result as a fraction
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 8248/825"""

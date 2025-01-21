"""
假令有股十六二分之一句弦相乘冪一百六十四二十五分之十四問句多少
術曰冪自乘為實股自乘為方法從開方除之所得又開方即句
答曰句 a 
"""

"""
Suppose there is a right triangle where the leg (gu) is 16 1/2 (16.5), and the product of the other leg (ju) and the hypotenuse (xian) is 164 14/25 (164.56).
Question: what is the length of the other leg (ju)?

The procedure says: Square the given product (mi), obtaining the dividend (shi). 
Square the given leg (gu), obtaining the divisor (fangfa). 
Divide the dividend by the divisor, and take the square root of the result. This is the length of the other leg (ju).

Answer: the other leg (ju) is *a*.
"""

from fractions import Fraction

# 股十六二分之一
股 = Fraction(33, 2)

# 冪一百六十四二十五分之十四
冪 = Fraction(164 * 25 + 14, 25)

# 冪自乘為實
實 = 冪 * 冪

# 股自乘為方法
方法 = 股 * 股

# 從開方除之所得
所得 = 實 / 方法

# 又開方即句
a = 所得 ** Fraction(1, 2)  # Square root of the result
"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 9.973333333333334"""

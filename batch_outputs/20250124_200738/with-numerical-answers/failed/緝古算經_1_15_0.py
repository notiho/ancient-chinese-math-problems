"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a(=1147/10) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and the base (ju) is 4036 and 1/5. 
The base (ju) is smaller than the hypotenuse (xian) by 6 and 1/5.
Question: how long is the hypotenuse?

The procedure says: Square the product (mi), double the smaller number (the difference), and add 1 to obtain the dividend.
Take half of the smaller number as the divisor (lianfa).
Divide the dividend by the divisor to obtain the base (ju).
Add the difference to the base to obtain the hypotenuse (xian).

Answer: the hypotenuse is *a*(=1147/10).
"""

from fractions import Fraction

# 冪四千三十六五分之□
冪 = Fraction(4036, 5)

# 股少於弦六五分之一
差 = Fraction(6, 5)

# 冪自乘
冪平方 = 冪 * 冪

# 倍少數而一，為實
實 = 2 * 差 * 冪平方 + 1

# 半少，為廉法
廉法 = 差 / 2

# 開立方除之，即股
股 = 實 / 廉法

# 加差，即弦
a = 股 + 差  # 1147/10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 195471767/75"""

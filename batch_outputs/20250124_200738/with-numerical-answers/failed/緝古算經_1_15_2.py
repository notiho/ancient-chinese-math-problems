"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a(=1147/10) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (gu) and the height (ju) equals 4036 and 1/5 (4036 + 1/5).
The height (gu) is smaller than the hypotenuse (xian) by 6 and 1/5 (6 + 1/5).
Question: what is the length of the hypotenuse?

The procedure says: Multiply the given product (mi) by itself. Double the smaller difference (cha) and add 1, obtaining the dividend.
Half the smaller difference is the divisor (lianfa). Divide the dividend by the divisor, obtaining the height (gu).
Add the smaller difference (cha) to the height (gu), obtaining the hypotenuse (xian).

Answer: the hypotenuse is *a*(=1147/10).
"""

from fractions import Fraction

# 冪四千三十六五分之□
冪 = Fraction(4036, 1) + Fraction(1, 5)

# 股少於弦六五分之一
差 = Fraction(6, 1) + Fraction(1, 5)

# 冪自乘
冪自乘 = 冪 * 冪

# 倍少數而一，為實
實 = 2 * 差 + 1

# 半少，為廉法
廉法 = 差 / 2

# 從。開立方除之，即股
股 = 冪自乘 / 廉法

# 加差，即弦
弦 = 股 + 差

a = 弦  # 1147/10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 26275693/5"""

"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a(=1147/10) 。
"""

"""
Suppose there is a right triangle where the product of the legs (ju and gu) is 4036 and 1/5.
The gu is smaller than the hypotenuse (xian) by 6 and 1/5.
Question: how long is the hypotenuse?

The procedure says: Square the product of the legs (mi), double the smaller difference, and add 1 to form the dividend.
Take half of the smaller difference as the divisor.
Extract the cube root of the division result to find gu.
Add the difference to gu to find the hypotenuse.

Answer: the hypotenuse is *a*(=1147/10).
"""

from fractions import Fraction

# 冪四千三十六五分之□
冪 = Fraction(4036, 5)

# 股少於弦六五分之一
差 = Fraction(31, 5)

# 術曰：冪自乘
冪平方 = 冪 * 冪

# 倍少數而一，為實
實 = 2 * 差 + 1
實 *= 冪平方

# 半少，為廉法，從
廉法 = 差 / 2

# 開立方除之，即股
股 = (實 / 廉法) ** Fraction(1, 3)

# 加差，即弦
弦 = 股 + 差

a = 弦  # 1147/10
"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 147.42181983289754"""

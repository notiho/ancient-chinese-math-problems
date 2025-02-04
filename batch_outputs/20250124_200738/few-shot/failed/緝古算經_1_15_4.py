"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gou) and the other leg (gu) is 4036 and 1/5 (4036 + 1/5).
The difference between the hypotenuse (xian) and the longer leg (gu) is 6 and 1/5 (6 + 1/5).
Question: what is the length of the hypotenuse?

The procedure says: Take the product (mi) and multiply it by itself. Double the smaller difference and add 1, obtaining the divisor.
Take half of the smaller difference as the gou divisor.
Divide the cube root of the product by the divisor, obtaining the gu. Add the difference to obtain the xian.

Answer: the hypotenuse is *a*.
"""

from fractions import Fraction

# 冪四千三十六五分之□
冪 = 4036 + Fraction(1, 5)

# 股少於弦六五分之一
差 = 6 + Fraction(1, 5)

# 冪自乘
冪平方 = 冪 * 冪

# 倍少數而一，為實
實 = 2 * 差 + 1

# 半少，為廉法，從
廉法 = 差 / 2

# 開立方除之，即股
股 = 冪平方 / (廉法 * 實)

# 加差，即弦
弦 = 股 + 差

a = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 131380387/335"""

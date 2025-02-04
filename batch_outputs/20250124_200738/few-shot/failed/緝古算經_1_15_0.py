"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and the other leg (ju) is 4036 and 1/5. 
The shorter leg (gu) is less than the hypotenuse (xian) by 6 and 1/5.
Question: how long is the hypotenuse?

The procedure says: Square the product (mi), double the smaller difference, and add 1 to obtain the dividend (shi). 
Take half of the smaller difference as the divisor (lianfa). 
Extract the cube root of the division result to obtain the shorter leg (gu). 
Add the difference to obtain the hypotenuse (xian).

Answer: the hypotenuse is *a*.
"""

from fractions import Fraction

# 冪四千三十六五分之□
冪 = Fraction(4036, 5)

# 股少於弦六五分之一
差 = Fraction(6, 5)

# 冪自乘
冪平方 = 冪 * 冪

# 倍少數而一，為實
實 = 2 * 差 + 1
實 *= 冪平方

# 半少，為廉法
廉法 = 差 / 2

# 從。開立方除之，即股
股 = (實 / 廉法) ** Fraction(1, 3)

# 加差，即弦
弦 = 股 + 差

a = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 155.7598393645504"""

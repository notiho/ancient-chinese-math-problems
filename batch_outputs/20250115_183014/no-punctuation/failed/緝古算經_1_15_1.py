"""
假令有句股相乘冪四千三十六五分之□股少於弦六五分之一問弦多少
術曰冪自乘倍少數而一為實半少為廉法從開立方除之即股加差即弦
答曰弦 a 
"""

"""
Suppose there is a right triangle where the product of the base (gu) and the height (ju) is 4036 1/5. 
The height (gu) is less than the hypotenuse (xian) by 6 1/5. 
Question: how long is the hypotenuse?

The procedure says: 
Take the square of the product (mi), double the smaller difference, and add 1 to form the dividend (shi). 
Take half of the smaller difference as the divisor (lianfa). 
Extract the cube root of the division result, and this is the height (gu). 
Add the difference to the height to obtain the hypotenuse.

Answer: the hypotenuse is *a*.
"""

from fractions import Fraction

# 冪四千三十六五分之
冪 = Fraction(4036, 1) + Fraction(1, 5)

# 股少於弦六五分之一
差 = Fraction(6, 1) + Fraction(1, 5)

# 冪自乘
冪平方 = 冪 * 冪

# 倍少數而一為實
實 = 2 * 差 + 1
實 *= 冪平方

# 半少為廉法
廉法 = 差 / 2

# 從開立方除之即股
股 = (實 / 廉法) ** Fraction(1, 3)

# 股加差即弦
弦 = 股 + 差

a = 弦
"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 419.1487478294179"""

"""
假令有句股相乘冪四千三十六五分之□股少於弦六五分之一問弦多少
術曰冪自乘倍少數而一為實半少為廉法從開立方除之即股加差即弦
答曰弦 a 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (gu) and the height (ju) is 4036 1/5.
The height (gu) is smaller than the hypotenuse (xian) by 6 1/5.
Question: what is the length of the hypotenuse?

The procedure says: Take the square of the product (mi), double it, subtract the square of the difference, and add 1 to obtain the dividend (shi).
Take half the difference as the divisor (lianfa).
Extract the cube root of the division result to obtain the height (gu).
Add the difference to the height to obtain the hypotenuse (xian).

Answer: The hypotenuse is *a*.
"""

from fractions import Fraction

# 冪四千三十六五分之一
冪 = Fraction(4036) + Fraction(1, 5)

# 股少於弦六五分之一
差 = Fraction(6) + Fraction(1, 5)

# 冪自乘
冪平方 = 冪 * 冪

# 倍少數
倍少數 = 2 * 差

# 倍少數而一為實
實 = 冪平方 - (倍少數 * 差) + 1

# 半少為廉法
廉法 = 差 / 2

# 從開立方除之即股
股 = Fraction(實, 廉法)

# 股加差即弦
弦 = 股 + 差

a = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 814542689/155"""

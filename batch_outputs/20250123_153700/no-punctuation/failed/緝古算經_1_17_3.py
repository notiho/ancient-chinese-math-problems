"""
假令有股弦相乘冪四千七百三十九五分之三句少於弦五十四五分之二問股多少
術曰冪自乘倍少數而一為立冪又少數再自乘半之以減立冪余為實又少數自乘倍之為方法又置少數五之二而一為廉法從開立方除之即句加差即弦弦除冪即股
答曰 a 
"""

"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 4739 and 3/5. 
The other leg (ju) is shorter than the hypotenuse by 54 and 2/5.
Question: how long is the other leg (gu)?

The procedure says:
1. Take the product (mi), square it, and double the shorter difference (shao shu), then add 1 to form the cubic power (li mi).
2. Square the shorter difference again, double it, and halve it. Subtract this from the cubic power to get the dividend (shi).
3. Square the shorter difference, double it, to form the divisor (fang fa).
4. Take the shorter difference, multiply it by 5, add 2, and add 1 to form the auxiliary divisor (lian fa).
5. Extract the cube root of the cubic power and divide by the auxiliary divisor to get the other leg (ju).
6. Add the shorter difference to the other leg to get the hypotenuse (xian).
7. Divide the product (mi) by the hypotenuse to get the leg (gu).

Answer: *a*.
"""

from fractions import Fraction

# 冪四千七百三十九五分之三
冪 = Fraction(4739) + Fraction(3, 5)

# 句少於弦五十四五分之二
少數 = Fraction(54) + Fraction(2, 5)

# 冪自乘倍少數而一為立冪
立冪 = 冪**2 + 2 * 冪 * 少數 + 1

# 少數再自乘半之以減立冪余為實
實 = 立冪 - (少數**2 * Fraction(1, 2))

# 少數自乘倍之為方法
方法 = 2 * 少數**2

# 置少數五之二而一為廉法
廉法 = 5 * 少數 + 2 + 1

# 從開立方除之即句
句 = (實 / 方法) ** Fraction(1, 3)

# 加差即弦
弦 = 句 + 少數

# 弦除冪即股
股 = 冪 / 弦

a = 股
"""
Variable 'a' has wrong value. Expected: 68, Actual: 67.59587593877697"""

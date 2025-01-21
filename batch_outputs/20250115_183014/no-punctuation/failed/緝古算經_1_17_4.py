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
1. Take the product of the leg and hypotenuse (mi), multiply it by itself, double the shorter difference, and add 1. This gives the cubic power (立冪).
2. Take the shorter difference, multiply it by itself twice, halve it, and subtract it from the cubic power. The remainder is the dividend (實).
3. Take the shorter difference, multiply it by itself, double it, and this becomes the divisor (方法).
4. Place the shorter difference, multiply it by 5, add 2, and add 1. This becomes the auxiliary divisor (廉法).
5. Extract the cube root of the cubic power, divide it by the divisor, and this gives the other leg (ju).
6. Add the shorter difference to the other leg (ju), and this gives the hypotenuse (xian).
7. Divide the product of the leg and hypotenuse (mi) by the hypotenuse (xian), and this gives the leg (gu).

Answer: *a*.
"""

from fractions import Fraction

# 冪 (mi) = 股弦相乘 = 4739 五分之三
冪 = 4739 + Fraction(3, 5)

# 少數 (difference between 弦 and 句) = 54 五分之二
少數 = 54 + Fraction(2, 5)

# Step 1: 冪自乘倍少數而一為立冪
立冪 = (冪 ** 2) * (2 * 少數 + 1)

# Step 2: 少數再自乘半之以減立冪余為實
實 = 立冪 - (少數 ** 2) / 2

# Step 3: 少數自乘倍之為方法
方法 = (少數 ** 2) * 2

# Step 4: 置少數五之二而一為廉法
廉法 = (少數 * 5) + 2 + 1

# Step 5: 開立方 (cube root of 立冪) and divide by 方法 to get 句 (ju)
句 = (立冪 ** (1 / 3)) / 方法

# Step 6: 句加差即弦 (xian)
弦 = 句 + 少數

# Step 7: 弦除冪即股 (gu)
股 = 冪 / 弦

a = 股
"""
Variable 'a' has wrong value. Expected: 68, Actual: 86.76092344623025"""

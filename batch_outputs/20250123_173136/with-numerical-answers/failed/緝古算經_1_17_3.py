"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a(=68) 。
"""

"""
Suppose there is a right triangle where the product of the legs (gu and xian) is given as 4739 and 3/5. 
The difference between the hypotenuse (xian) and the shorter leg (ju) is 54 and 2/5.
Question: how long is the other leg (gu)?

The procedure says: Square the given product (mi), double the smaller number (the difference) and add 1, obtaining the cubic power (立冪).
Then, square the smaller number again, halve it, and subtract it from the cubic power, leaving the remainder as the dividend (實).
Square the smaller number again, double it, obtaining the divisor (方法).
Place the smaller number, multiply it by 5, and divide by 2, obtaining the edge divisor (廉法).
Extract the cube root of the dividend divided by the divisor, obtaining the shorter leg (ju).
Add the difference to the shorter leg, obtaining the hypotenuse (xian).
Divide the product by the hypotenuse, obtaining the other leg (gu).

Answer: *a*(=68).
"""

from fractions import Fraction

# 冪四千七百三十九五分之三
冪 = Fraction(4739) + Fraction(3, 5)

# 句少於弦五十四五分之二
少數 = Fraction(54) + Fraction(2, 5)

# 冪自乘
冪平方 = 冪 ** 2

# 倍少數而一，為立冪
立冪 = 2 * 少數 + 1

# 又少數再自乘
少數平方 = 少數 ** 2

# 半之，以減立冪，余為實
實 = 立冪 - (少數平方 / 2)

# 又少數自乘，倍之，為方法
方法 = 2 * 少數平方

# 又置少數，五之，二而一，為廉法
廉法 = (少數 * 5) / 2

# 開立方除之，即句
句 = (實 / 方法) ** Fraction(1, 3)

# 加差，即弦
弦 = 句 + 少數

# 弦除冪，即股
股 = 冪 / 弦

a = 股  # 68
"""
Variable 'a' has wrong value. Expected: 68, Actual: (86.627914823979-0.8419712526920703j)"""

"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a(=68) 。
"""

"""
Suppose there is a right triangle where the product of the legs and hypotenuse (the area of the square on the hypotenuse) is 4739 and 3/5. 
The shorter leg (句) is less than the hypotenuse (弦) by 54 and 2/5. 
Question: how long is the other leg (股)?

The procedure says: 
1. Square the given area (冪), double the difference (少數), and add 1 to form the cubic power (立冪).
2. Square the difference (少數) again, divide it by 2, and subtract it from the cubic power to get the remainder (實).
3. Square the difference (少數) again, double it, to form the divisor (方法).
4. Multiply the difference (少數) by 5, divide it by 2, to form the linear divisor (廉法).
5. Extract the cube root of the remainder (實), divide it by the divisor (方法), to get the shorter leg (句).
6. Add the difference (少數) to the shorter leg to get the hypotenuse (弦).
7. Divide the area (冪) by the hypotenuse to get the other leg (股).

Answer: *a*(=68).
"""

from fractions import Fraction

# 冪四千七百三十九五分之三
冪 = Fraction(4739 * 5 + 3, 5)

# 句少於弦五十四五分之二
少數 = Fraction(54 * 5 + 2, 5)

# 冪自乘
冪平方 = 冪 ** 2

# 倍少數而一，為立冪
立冪 = 冪平方 + 2 * 冪 * 少數 + 少數 ** 2

# 又少數再自乘，半之，以減立冪，余為實
實 = 立冪 - (少數 ** 2) / 2

# 又少數自乘，倍之，為方法
方法 = 2 * (少數 ** 2)

# 又置少數，五之，二而一，為廉法，從
廉法 = (少數 * 5) / 2

# 開立方除之，即句
句 = (實 ** (1 / 3)) / 方法

# 加差，即弦
弦 = 句 + 少數

# 弦除冪，即股
股 = 冪 / 弦

a = 股  # 68
"""
Variable 'a' has wrong value. Expected: 68, Actual: 87.04813614757693"""

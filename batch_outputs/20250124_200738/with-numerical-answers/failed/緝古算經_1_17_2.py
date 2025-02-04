"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a(=68) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the legs (gu and xian) is given as 4739 and 3/5.
The difference between the hypotenuse (xian) and the shorter leg (ju) is 54 and 2/5.
Question: how long is the other leg (gu)?

The procedure says:
1. Multiply the given product (mi) by itself, then double the smaller difference (shao shu) and add 1 to form the cubic power (li mi).
2. Square the smaller difference (shao shu) again, halve it, and subtract it from the cubic power to get the remainder (shi).
3. Square the smaller difference (shao shu) again, double it, to form the divisor (fang fa).
4. Multiply the smaller difference (shao shu) by 5, divide by 2, and add 1 to form the divisor (lian fa).
5. Extract the cube root of the remainder and divide it by the divisor to get the shorter leg (ju).
6. Add the difference to the shorter leg to get the hypotenuse (xian).
7. Divide the product (mi) by the hypotenuse to get the other leg (gu).

Answer: *a*(=68).
"""

from fractions import Fraction

# 冪四千七百三十九五分之三
冪 = Fraction(4739 * 5 + 3, 5)

# 句少於弦五十四五分之二
少數 = Fraction(54 * 5 + 2, 5)

# 冪自乘
立冪 = 冪 ** 2

# 倍少數而一
立冪 += 2 * 少數 + 1

# 少數再自乘
減項 = (少數 ** 2) / 2

# 半之，以減立冪
實 = 立冪 - 減項

# 少數自乘，倍之
方法 = 2 * (少數 ** 2)

# 置少數，五之，二而一
廉法 = (5 * 少數 + 2) / 2

# 開立方除之，即句
句 = (實 ** Fraction(1, 3)) / 廉法

# 加差，即弦
弦 = 句 + 少數

# 弦除冪，即股
股 = 冪 / 弦

a = 股 # 68#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 68, Actual: 83.94687694202048"""

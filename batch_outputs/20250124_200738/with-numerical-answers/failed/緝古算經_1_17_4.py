"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
術曰：冪自乘，倍少數而一，為立冪。又少數再自乘，半之，以減立冪，余為實。又少數自乘，倍之，為方法。又置少數，五之，二而一，為廉法，從。開立方除之，即句。加差，即弦。弦除冪，即股。
答曰： a(=68) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the legs (the base and the height) and the hypotenuse equals 4739 and 3/5. 
The base (句) is smaller than the hypotenuse (弦) by 54 and 2/5.
Question: how long is the other leg (股)?

The procedure says:
1. Multiply the product (冪) by itself, double the difference (少數), and add 1 to form the cubic power (立冪).
2. Multiply the difference (少數) by itself again, halve it, and subtract it from the cubic power to get the remainder (實).
3. Multiply the difference (少數) by itself, double it, to form the divisor (方法).
4. Place the difference (少數), multiply it by 5, and divide by 2 to form the auxiliary divisor (廉法).
5. Extract the cube root of the remainder (實) and divide it by the divisor (方法) to get the base (句).
6. Add the difference (少數) to the base (句) to get the hypotenuse (弦).
7. Divide the product (冪) by the hypotenuse (弦) to get the other leg (股).

Answer: *a*(=68).
"""

from fractions import Fraction

# 冪四千七百三十九五分之三
冪 = Fraction(4739 * 5 + 3, 5)

# 句少於弦五十四五分之二
少數 = Fraction(54 * 5 + 2, 5)

# 冪自乘
冪自乘 = 冪 * 冪

# 倍少數而一，為立冪
立冪 = 冪自乘 + 2 * 少數 + 1

# 又少數再自乘，半之，以減立冪，余為實
少數自乘 = 少數 * 少數
實 = 立冪 - (少數自乘 / 2)

# 又少數自乘，倍之，為方法
方法 = 2 * 少數自乘

# 又置少數，五之，二而一，為廉法
廉法 = (少數 * 5) / 2

# 開立方除之，即句
句 = Fraction(實, 方法)

# 加差，即弦
弦 = 句 + 少數

# 弦除冪，即股
股 = 冪 / 弦

a = 股 # 68#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 68, Actual: 3506545664/2848052081"""

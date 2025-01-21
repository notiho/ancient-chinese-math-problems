"""
又有弧田，弦七十八步、二分步之一，矢十三步、九分步之七。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a segment of a circle (弧田) using the given formula. Here's the Python code:


"""


from fractions import Fraction

# Given values
chord = Fraction(78, 1) + Fraction(1, 2)  # 弦 = 78步 + 1/2步
arrow = Fraction(13, 1) + Fraction(7, 9)  # 矢 = 13步 + 7/9步

# Calculation
a = (chord * arrow + arrow * arrow) / 2  # 田 = (弦 * 矢 + 矢^2) / 2

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 畝 (mu).
"""


"""
Variable 'a' has wrong value. Expected: 51491/19440, Actual: 51491/81"""

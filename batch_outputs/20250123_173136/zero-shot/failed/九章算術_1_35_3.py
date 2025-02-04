"""
又有弧田，弦七十八步、二分步之一，矢十三步、九分步之七。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular segment (弧田) using the given formula. Here's the Python code:


"""


from fractions import Fraction

# Given values
chord = Fraction(78, 1) + Fraction(1, 2)  # 弦: 78步, 二分步之一
arrow = Fraction(13, 1) + Fraction(7, 9)  # 矢: 13步, 九分步之七

# Calculation
area = (chord * arrow + arrow * arrow) / 2  # 以弦乘矢，矢又自乘，并之，二而一

# Answer
a = area  # 荅曰：a畝


"""


The variable `a` will hold the area of the field in terms of 畝 (ancient Chinese unit of area).
"""


"""
Variable 'a' has wrong value. Expected: 51491/19440, Actual: 51491/81"""

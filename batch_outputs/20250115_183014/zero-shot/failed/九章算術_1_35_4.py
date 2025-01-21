"""
又有弧田，弦七十八步、二分步之一，矢十三步、九分步之七。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a circular segment (弧田) where the chord (弦) and the sagitta (矢) are given, and we need to calculate the area of the segment (田). The formula provided is:

1. Multiply the chord (弦) by the sagitta (矢).
2. Square the sagitta (矢) and add it to the result of step 1.
3. Divide the result by 2 to get the area.

Here is the Python code:


"""


from fractions import Fraction

# Given values
chord = Fraction(78, 1) + Fraction(1, 2)  # 弦: 78步, 二分步之一
sagitta = Fraction(13, 1) + Fraction(7, 9)  # 矢: 13步, 九分步之七

# Calculation
area = (chord * sagitta + sagitta * sagitta) / 2

# Solution
a = area  # The area in 畝


"""


The variable `a` will contain the area of the segment in 畝 (a traditional Chinese unit of area).
"""


"""
Variable 'a' has wrong value. Expected: 51491/19440, Actual: 51491/81"""

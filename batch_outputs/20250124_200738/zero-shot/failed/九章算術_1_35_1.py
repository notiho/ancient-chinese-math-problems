"""
又有弧田，弦七十八步、二分步之一，矢十三步、九分步之七。問：為田幾何？
術曰：以弦乘矢，矢又自乘，并之，二而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a circular segment field (弧田), where the chord (弦) and the sagitta (矢) are given. The area of the field is calculated using the formula described in the problem.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
chord = Fraction(78, 1) + Fraction(1, 2)  # 弦: 78步, 二分步之一
sagitta = Fraction(13, 1) + Fraction(7, 9)  # 矢: 13步, 九分步之七

# Calculation
area = (chord * sagitta + sagitta * sagitta) / 2  # 以弦乘矢，矢又自乘，并之，二而一

# Answer
a = area  # a畝
#----- content ends here -----


"""


The variable `a` will contain the area of the field in the appropriate units (畝).
"""


"""
Variable 'a' has wrong value. Expected: 51491/19440, Actual: 51491/81"""

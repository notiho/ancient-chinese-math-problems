"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the area of the field. The problem gives the dimensions of the field as fractions of steps, and we need to multiply them together. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the field
length = Fraction(7, 1) + Fraction(3, 4)  # 7 steps and 3/4 of a step
width = Fraction(15, 1) + Fraction(5, 9)  # 15 steps and 5/9 of a step

# Area of the field
a = length * width

# Result
a  # The area in steps squared
#----- content ends here -----


"""


This will compute the value of `a` as the area of the field in terms of steps squared.
"""


"""
"""

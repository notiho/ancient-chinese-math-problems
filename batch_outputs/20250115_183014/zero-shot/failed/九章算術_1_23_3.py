"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of the field based on the given dimensions. The dimensions are given as fractions of steps, and the area is calculated by multiplying the two dimensions together.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Dimensions of the field
length = Fraction(18) + Fraction(5, 7)  # 18 steps and 5/7 of a step
width = Fraction(23) + Fraction(6, 11)  # 23 steps and 6/11 of a step

# Area of the field
a = length * width

# The result is stored in the variable `a`


"""


The variable `a` will contain the area of the field in square steps as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 4847/2640, Actual: 4847/11"""

"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves fractions and their operations. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
broad_field = Fraction(18, 1) + Fraction(5, 7)  # 18 steps and 5/7 of a step
long_field = Fraction(23, 1) + Fraction(6, 11)  # 23 steps and 6/11 of a step

# Area calculation
a = broad_field * long_field  # Area of the field in square steps

# Result
a  # The area in square steps
#----- content ends here -----


"""


The variable `a` will hold the area of the field in terms of square steps.
"""


"""
Variable 'a' has wrong value. Expected: 4847/2640, Actual: 4847/11"""

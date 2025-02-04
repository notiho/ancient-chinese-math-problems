"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to compute the area of the field. The problem involves fractions and subtraction. Let's translate the problem into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
length = Fraction(18) + Fraction(5, 7)  # 18 steps and 5/7 of a step
width = Fraction(23) + Fraction(6, 11)  # 23 steps and 6/11 of a step

# Area calculation
a = length * width  # Area in square steps

# Result
a  # The area of the field in square steps
#----- content ends here -----


"""


This code computes the area of the field (`a`) in square steps using the given dimensions. The result will be stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 4847/2640, Actual: 4847/11"""

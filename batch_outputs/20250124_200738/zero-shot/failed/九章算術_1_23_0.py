"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of the field. The problem involves fractions of steps, and the solution requires multiplying and dividing fractions. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
length = Fraction(18) + Fraction(5, 7)  # 18 steps and 5/7 of a step
width = Fraction(23) + Fraction(6, 11)  # 23 steps and 6/11 of a step

# Calculate the area
a = length * width

# The result is stored in the variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in terms of "畝".
"""


"""
Variable 'a' has wrong value. Expected: 4847/2640, Actual: 4847/11"""

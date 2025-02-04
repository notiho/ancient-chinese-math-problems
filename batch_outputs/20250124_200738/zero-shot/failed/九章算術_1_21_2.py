"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will compute the total area of the field by adding the two given areas. The areas are expressed as fractions of steps (步). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given areas
area1 = Fraction(3, 1) + Fraction(1, 3)  # 3步 + 1/3步
area2 = Fraction(5, 1) + Fraction(2, 5)  # 5步 + 2/5步

# Total area
a = area1 + area2

# The answer
a  # a步
#----- content ends here -----


"""


This will compute the value of `a` in terms of steps (步).
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 131/15"""

"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will compute the total area of the field by adding the two given areas. The areas are expressed as fractions of steps (步). Let's translate the problem into Python code:


"""


from fractions import Fraction

# Given areas
area1 = Fraction(3, 1) + Fraction(1, 3)  # 3步 + 3分步之一
area2 = Fraction(5, 1) + Fraction(2, 5)  # 5步 + 5分步之二

# Total area
a = area1 + area2

# Result
a  # This is the total area in steps (步)


"""


The variable `a` will hold the total area of the field in steps (步).
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 131/15"""

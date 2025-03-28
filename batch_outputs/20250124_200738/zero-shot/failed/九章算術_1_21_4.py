"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve the problem, we translate the ancient Chinese math problem into Python code. The problem involves fractions and their operations. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
field1 = Fraction(3, 1) + Fraction(1, 3)  # 3步, 3分步之一
field2 = Fraction(5, 1) + Fraction(2, 5)  # 5步, 5分步之二

# Total field area
a = field1 + field2  # Combine the two fields

# The result
a  # The total area in steps
#----- content ends here -----


"""


The variable `a` will contain the total area of the field in steps.
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 131/15"""

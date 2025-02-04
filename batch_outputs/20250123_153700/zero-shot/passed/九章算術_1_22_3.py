"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves fractions and operations on them. Here's the solution:


"""


from fractions import Fraction

# Given values
broad_field = Fraction(7, 1) + Fraction(3, 4)  # 7 steps + 3/4 steps
long_field = Fraction(15, 1) + Fraction(5, 9)  # 15 steps + 5/9 steps

# Multiplying the two fractions to find the area
a = broad_field * long_field  # Area of the field

# Output the result
a  # The area in steps²


"""


The variable `a` will contain the area of the field in terms of steps² as a `Fraction`.
"""


"""
"""

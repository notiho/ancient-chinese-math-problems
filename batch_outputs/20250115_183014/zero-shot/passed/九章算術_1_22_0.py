"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves fractions and their operations. Here's the solution:


"""


from fractions import Fraction

# Given values
田廣 = Fraction(7, 1) + Fraction(3, 4)  # 7步 and 4分步之3
從 = Fraction(15, 1) + Fraction(5, 9)   # 15步 and 9分步之5

# Calculation for the area of the field
a = 田廣 * 從

# Result
a  # This will give the area in terms of steps (步)


"""


The variable `a` will contain the computed value of the area of the field in terms of steps (步).
"""


"""
"""

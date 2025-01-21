"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves subtracting two fractional areas of land to find the remaining area. Here's the Python code:


"""


from fractions import Fraction

# Given values
area1 = Fraction(18, 1) + Fraction(5, 7)  # 18 steps + 5/7 steps
area2 = Fraction(23, 1) + Fraction(6, 11)  # 23 steps + 6/11 steps

# Subtract the areas
a = area1 - area2

# The result is stored in variable 'a'
a  # This represents the remaining area in steps


"""


The variable `a` will contain the result of the calculation, representing the remaining area in fractional steps.
"""


"""
Variable 'a' has wrong value. Expected: 4847/2640, Actual: -372/77"""

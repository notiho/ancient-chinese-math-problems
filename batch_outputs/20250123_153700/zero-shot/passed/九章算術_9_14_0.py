"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a步 。
"""

"""
This problem is a classic right triangle problem, where the "句" (base) and "股" (height) are given, and we are tasked to find the area of the square inscribed in the triangle. Here's the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
句 = 5  # base in steps
股 = 12  # height in steps

# Compute the area of the square inscribed in the triangle
實 = 句 * 股  # area of the rectangle formed by base and height
法 = 句 + 股  # sum of base and height
a = Fraction(實, 法)  # area of the square (in steps squared)

# The answer
a  # area in steps squared


"""

"""


"""
"""

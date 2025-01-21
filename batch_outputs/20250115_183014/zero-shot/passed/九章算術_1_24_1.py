"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that the area of a rectangular field is calculated by multiplying half the width (廣) by the length (正從). Here's the Python code:


"""


from fractions import Fraction

# Given values
廣 = 12  # Width in steps
正從 = 21  # Length in steps

# Calculation
a = Fraction(廣, 2) * 正從  # Area in steps^2

# Result
a  # Area of the field in steps^2


"""


The variable `a` will store the area of the field in steps².
"""


"""
"""

"""
今有覆月田從三十步徑十步。問：為田㡬何？
術曰：列徑十步半之得五步以從三十步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem describes a circular field with a diameter of 10 steps and a circumference of 30 steps. The goal is to calculate the area of the field in square steps.

Here is the Python code:


"""


from fractions import Fraction

# Given values
diameter = 10  # steps
circumference = 30  # steps

# Calculation
radius = Fraction(diameter, 2)  # radius is half of the diameter
a = radius * circumference  # area of the field

# Result
a  # in square steps


"""


The variable `a` will hold the area of the field in square steps.
"""


"""
"""

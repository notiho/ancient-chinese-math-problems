"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a步 。
"""

"""
This problem describes a circular field where the circumference ("周") is 30 steps and the diameter ("徑") is 16 steps. The goal is to calculate the area of the field ("田") using the formula provided: multiply the circumference by the diameter, then divide by 4.

Here is the Python code to compute the value of "a":


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 30  # 周 (steps)
diameter = 16       # 徑 (steps)

# Calculation
a = Fraction(circumference * diameter, 4)  # Area of the field (steps^2)

# Result
a  # The area in steps^2
#----- content ends here -----


"""


The variable `a` will hold the area of the field in square steps.
"""


"""
"""

"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
術曰：并內外周得四十二步半之得二十一步以徑三步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of an annular field (a ring-shaped field). The outer circumference is 30 steps, the inner circumference is 12 steps, and the diameter of the ring is 3 steps.

The solution involves the following steps:
1. Add the outer and inner circumferences together.
2. Divide the sum by 2 to get the average circumference.
3. Multiply the average circumference by the diameter to compute the area.

Here is the Python code:


"""


from fractions import Fraction

# Given values
outer_circumference = Fraction(30)  # Outer circumference in steps
inner_circumference = Fraction(12)  # Inner circumference in steps
diameter = Fraction(3)  # Diameter in steps

# Compute the average circumference
average_circumference = (outer_circumference + inner_circumference) / 2

# Compute the area of the annular field
a = average_circumference * diameter

# The result is stored in variable 'a'
a  # Area in steps


"""


The variable `a` will contain the area of the annular field in steps.
"""


"""
"""

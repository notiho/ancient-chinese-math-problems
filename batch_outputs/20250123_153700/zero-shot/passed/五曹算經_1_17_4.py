"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
術曰：并內外周得四十二步半之得二十一步以徑三步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of the ring-shaped field (環田). The problem provides the outer circumference (外周), inner circumference (內周), and the diameter (徑). The formula for the area of a ring is derived from the difference between the areas of the outer and inner circles.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
outer_circumference = Fraction(30)  # 外周三十步
inner_circumference = Fraction(12)  # 內周一十二步
diameter = Fraction(3)  # 徑三步

# Calculate the average circumference (並內外周得四十二步半之得二十一步)
average_circumference = (outer_circumference + inner_circumference) / 2

# Multiply the average circumference by the diameter to get the area
a = average_circumference * diameter

# The area of the ring-shaped field is stored in variable 'a'


"""


The value of `a` will be the area of the field in square steps (步²).
"""


"""
"""

"""
今有圓田，周三十步，徑十步。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a步 。
"""

"""
To solve this problem, we are given a circular field with a circumference ("周") of 30 steps ("步") and a diameter ("徑") of 10 steps. The formula provided states that the area of the field is calculated by multiplying half the circumference by half the diameter.

Here is the Python code to compute the area:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 30  # 周, in steps
diameter = 10       # 徑, in steps

# Calculate half the circumference and half the diameter
half_circumference = Fraction(circumference, 2)
half_diameter = Fraction(diameter, 2)

# Compute the area
a = half_circumference * half_diameter  # Area in steps^2

# The result is stored in variable 'a'
#----- content ends here -----


"""


The area of the circular field is stored in the variable `a` as a fraction in steps².
"""


"""
"""

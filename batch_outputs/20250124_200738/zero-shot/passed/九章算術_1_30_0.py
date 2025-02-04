"""
今有圓田，周三十步，徑十步。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field. The problem states that the circumference (周) is 30 steps (步), and the diameter (徑) is 10 steps (步). The formula provided in the problem is to multiply half the circumference by half the diameter to get the area.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 30  # in steps
diameter = 10  # in steps

# Calculations
half_circumference = Fraction(circumference, 2)  # 半周
half_diameter = Fraction(diameter, 2)  # 半徑

# Area calculation
a = half_circumference * half_diameter  # 半周半徑相乘得積步

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the area of the circular field in steps squared (步²).
"""


"""
"""

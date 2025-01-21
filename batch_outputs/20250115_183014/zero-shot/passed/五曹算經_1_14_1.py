"""
今有覆月田從三十步徑十步。問：為田㡬何？
術曰：列徑十步半之得五步以從三十步乘之即得。
答曰： a步 。
"""

"""
This problem involves calculating the area of a circular field (覆月田). The diameter is given as 10 steps (步), so the radius is half of that, which is 5 steps. The circumference is given as 30 steps. The area is calculated using the formula for the area of a circle, which is approximately \( \text{radius} \times \text{circumference} \).

Here is the Python code to compute the area:


"""


from fractions import Fraction

# Given values
radius = Fraction(10, 2)  # Radius is half of the diameter
circumference = Fraction(30)  # Circumference in steps

# Calculate the area
a = radius * circumference  # Area formula: radius * circumference

# The result is stored in variable 'a'


"""


The area of the field is stored in the variable `a` in units of steps squared (步²).
"""


"""
"""

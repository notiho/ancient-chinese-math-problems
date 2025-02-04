"""
今有覆月田從三十步徑十步。問：為田㡬何？
術曰：列徑十步半之得五步以從三十步乘之即得。
答曰： a步 。
"""

"""
This problem involves calculating the area of a circular field. The diameter of the circle is given as 10 steps, and the circumference is 30 steps. The solution involves finding the area of the field.

Here is the Python code to compute the value of the unknown `a`:


"""


from fractions import Fraction

# Given values
diameter = 10  # steps
circumference = 30  # steps

# Calculate the radius (half of the diameter)
radius = Fraction(diameter, 2)

# Calculate the area of the circular field
a = radius * circumference

# The result is stored in variable 'a'


"""


The variable `a` will contain the area of the circular field in steps².
"""


"""
"""

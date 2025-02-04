"""
今有圓田，周三十步，徑十步。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a步 。
"""

"""
To solve the problem, we need to calculate the area of a circular field. The problem states that the circumference is 30 steps and the diameter is 10 steps. The formula for the area of a circle is given as "半周半徑相乘得積步" (half the circumference multiplied by the radius).

Here is the Python code:


"""


from fractions import Fraction

# Given values
circumference = 30  # steps
diameter = 10  # steps

# Calculate radius
radius = Fraction(diameter, 2)

# Calculate half the circumference
half_circumference = Fraction(circumference, 2)

# Calculate the area
a = half_circumference * radius

# The result is stored in variable 'a'


"""


The variable `a` will contain the area of the circular field in steps².
"""


"""
"""

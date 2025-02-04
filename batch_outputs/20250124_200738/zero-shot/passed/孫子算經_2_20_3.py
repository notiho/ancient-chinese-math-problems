"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
術曰：半周得三百一十九步五分半徑，得一百九十步二位相乘，得六萬七百五步，以畝法除之，即得。
答曰： a頃 。
"""

"""
To solve this problem, we need to calculate the area of a circular field given its circumference and diameter in steps. The problem states that the circumference is 639 steps and the diameter is 380 steps. The area is then calculated using the formula for the area of a circle, \( \text{Area} = \pi r^2 \), but in this case, the ancient method uses an approximation.

Here is the Python code to compute the value of \( a \) (the area in "頃"):


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 639  # in steps
diameter = 380  # in steps

# Step 1: Calculate the radius
radius = Fraction(diameter, 2)

# Step 2: Multiply half the circumference by the radius
half_circumference = Fraction(circumference, 2)
area_in_steps = half_circumference * radius

# Step 3: Convert steps to "畝" (ancient Chinese unit of area)
# 1 畝 = 240 steps^2
area_in_mu = area_in_steps / 240

# Step 4: Convert "畝" to "頃" (1 頃 = 100 畝)
a = area_in_mu / 100

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` now contains the area of the field in "頃" as a `Fraction`.
"""


"""
"""

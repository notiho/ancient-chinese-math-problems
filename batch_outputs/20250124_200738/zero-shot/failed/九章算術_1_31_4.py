"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of a circular field. The problem provides the circumference ("周") and the diameter ("徑"). The formula for the area of a circle is given as:

\[
\text{Area} = \frac{\text{Circumference}}{2} \times \frac{\text{Diameter}}{2}
\]

This formula is derived from the relationship between the circumference, diameter, and radius of a circle. The units of the result will be in "畝" (a traditional Chinese unit of area).

Here is the Python code to compute the area:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = Fraction(180)  # 周: 180 steps
diameter = Fraction(60) + Fraction(1, 3)  # 徑: 60 steps + 1/3 step

# Calculating the radius
radius = diameter / 2

# Calculating the area
a = (circumference / 2) * radius

# The result is stored in the variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the circular field in "畝".
"""


"""
Variable 'a' has wrong value. Expected: 32761/2880, Actual: 2715"""

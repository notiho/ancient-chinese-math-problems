"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a circular field where the circumference (周) is 180.5 steps, and the diameter (徑) is 60 + 1/3 steps. We are tasked to calculate the area of the field in "畝" (a traditional Chinese unit of area).

The formula provided in the problem states that the area is calculated by multiplying half the circumference (半周) by half the diameter (半徑). Let's compute this:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = Fraction(1805, 10)  # 180.5 steps
diameter = Fraction(60) + Fraction(1, 3)  # 60 + 1/3 steps

# Calculate half the circumference and half the diameter
half_circumference = circumference / 2
half_diameter = diameter / 2

# Calculate the area in 畝
a = half_circumference * half_diameter

# Output the result
a  # This is the area in 畝
#----- content ends here -----


"""


The variable `a` will contain the area of the circular field in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 32761/2880, Actual: 65341/24"""

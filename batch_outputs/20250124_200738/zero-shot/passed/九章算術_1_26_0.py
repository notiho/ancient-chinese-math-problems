"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field (邪田) with one side 30 steps wide, the other side 42 steps wide, and a perpendicular height (正從) of 64 steps. The goal is to calculate the area of the field in 畝 (a traditional Chinese unit of area).

The formula provided in the problem can be interpreted as follows:
1. Add the two parallel sides (30 and 42), divide by 2 to get the average width.
2. Multiply the average width by the height (64 steps) to get the area in square steps.
3. Convert the area from square steps to 畝 using the conversion factor (1 畝 = 240 square steps).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
side1 = 30  # in steps
side2 = 42  # in steps
height = 64  # in steps
conversion_factor = 240  # 1 畝 = 240 square steps

# Calculate the area in 畝
average_width = Fraction(side1 + side2, 2)  # Average of the two sides
area_in_square_steps = average_width * height  # Area in square steps
a = area_in_square_steps / conversion_factor  # Convert to 畝

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""

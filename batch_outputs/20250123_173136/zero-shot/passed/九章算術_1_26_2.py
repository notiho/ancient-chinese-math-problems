"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field with one side 30 steps wide, the other side 42 steps wide, and the height (or perpendicular distance between the two parallel sides) 64 steps. The goal is to calculate the area of the field in terms of "畝" (a traditional Chinese unit of area).

The formula provided in the problem can be interpreted as follows:
1. Add the two parallel sides (30 and 42), divide by 2 to get the average width.
2. Multiply the average width by the height (64 steps) to get the area in square steps.
3. Convert the area in square steps to "畝" using the conversion factor (1 畝 = 240 square steps).

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions of the trapezoidal field
side1 = 30  # in steps
side2 = 42  # in steps
height = 64  # in steps

# Step 1: Compute the average width
average_width = Fraction(side1 + side2, 2)

# Step 2: Compute the area in square steps
area_in_square_steps = average_width * height

# Step 3: Convert the area to 畝 (1 畝 = 240 square steps)
a = area_in_square_steps / 240

# The result is stored in variable 'a'


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""

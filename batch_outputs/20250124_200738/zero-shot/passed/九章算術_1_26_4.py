"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a trapezoidal field where one base is 30 steps wide, the other base is 42 steps wide, and the height (or perpendicular distance between the bases) is 64 steps. The area of the field is to be calculated in units of "畝" (a traditional Chinese unit of area).

The formula provided in the problem can be interpreted as the area of a trapezoid:
1. Add the two bases together and divide by 2 to get the average width.
2. Multiply the average width by the height to get the area in square steps.
3. Convert the area from square steps to "畝" using the conversion factor (1 畝 = 240 square steps).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
base1 = 30  # steps
base2 = 42  # steps
height = 64  # steps

# Step 1: Calculate the average width
average_width = Fraction(base1 + base2, 2)

# Step 2: Calculate the area in square steps
area_in_square_steps = average_width * height

# Step 3: Convert the area to 畝 (1 畝 = 240 square steps)
a = area_in_square_steps / 240

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the area of the field in 畝 as a `Fraction`.
"""


"""
"""

"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
術曰：令徑二尺五寸自乘，以七寸自乘減之，其餘開方除之，即廣。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a circular material with a diameter of 2 feet 5 inches (2.5 feet) and a thickness of 7 inches (0.5833 feet). We are tasked with finding the side length of a square board that can be made from this material.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
diameter = Fraction(25, 10)  # 2 feet 5 inches = 2.5 feet
thickness = Fraction(7, 12)  # 7 inches = 7/12 feet

# Step 1: Square the diameter
diameter_squared = diameter * diameter

# Step 2: Square the thickness
thickness_squared = thickness * thickness

# Step 3: Subtract the square of the thickness from the square of the diameter
remaining_area = diameter_squared - thickness_squared

# Step 4: Take the square root of the remaining area to find the side length of the square
a = Fraction(math.sqrt(remaining_area))

# The side length of the square board is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the side length of the square board in feet.
"""


"""
Variable 'a' has wrong value. Expected: 12/5, Actual: 2737053693697313/1125899906842624"""

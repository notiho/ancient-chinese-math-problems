"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
術曰：令徑二尺五寸自乘，以七寸自乘減之，其餘開方除之，即廣。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a circular material with a diameter of 2 feet 5 inches (or 2.5 feet, since 1 foot = 10 inches in ancient Chinese measurements). We are tasked with determining the side length of a square board ("廣") that can be cut from this circular material, given that the thickness of the board is 7 inches (or 0.7 feet).

The formula provided states that we square the diameter, subtract the square of the thickness, and then take the square root of the result to find the side length of the square board.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
diameter = Fraction(25, 10)  # 2 feet 5 inches = 2.5 feet
thickness = Fraction(7, 10)  # 7 inches = 0.7 feet

# Calculation
diameter_squared = diameter ** 2
thickness_squared = thickness ** 2
remaining_area = diameter_squared - thickness_squared
a = math.sqrt(float(remaining_area))  # Taking the square root to find the side length

# Convert the result back to a Fraction for precision
a = Fraction(a).limit_denominator()

# The side length of the square board is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` represents the side length of the square board in feet.
"""


"""
"""

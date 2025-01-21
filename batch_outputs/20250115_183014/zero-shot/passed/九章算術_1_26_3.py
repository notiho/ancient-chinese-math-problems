"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a trapezoidal field with one base width of 30 steps, the other base width of 42 steps, and a height (perpendicular distance between the bases) of 64 steps. The goal is to calculate the area of the field in terms of "畝" (a traditional Chinese unit of area).

Here is the Python code:


"""


from fractions import Fraction

# Given values
base1 = 30  # in steps
base2 = 42  # in steps
height = 64  # in steps

# Compute the area in steps^2
average_base = Fraction(base1 + base2, 2)  # Average of the two bases
area_steps_squared = average_base * height  # Area in steps^2

# Convert steps^2 to 畝
# 1 畝 = 240 steps^2
a = area_steps_squared / 240  # Area in 畝

# The result is stored in the variable 'a'


"""


The variable `a` now contains the area of the field in 畝 as a `Fraction`.
"""


"""
"""

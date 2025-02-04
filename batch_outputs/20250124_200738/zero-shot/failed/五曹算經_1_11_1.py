"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to compute the area of a circular field given its circumference and diameter. The area is then converted into a unit of measurement called "頃" and "步". Here's the Python code to compute the values of `a` and `b`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 640  # 周六百四十步
diameter = 380       # 徑三百八十步

# Step 1: Compute half of the circumference and half of the diameter
half_circumference = Fraction(circumference, 2)
half_diameter = Fraction(diameter, 2)

# Step 2: Multiply the two halves to get the area in square steps
area_in_square_steps = half_circumference * half_diameter

# Step 3: Convert the area into "頃" and "步"
# 1 頃 = 24000 square steps
area_in_qing = area_in_square_steps // 24000
remaining_steps = area_in_square_steps % 24000

# Assign the results to variables
a = area_in_qing
b = remaining_steps

# Results
a, b
#----- content ends here -----


"""


This code calculates the values of `a` (in "頃") and `b` (remaining "步") based on the given problem.
"""


"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 2
Variable 'b' has wrong value. Expected: 80, Actual: 12800"""

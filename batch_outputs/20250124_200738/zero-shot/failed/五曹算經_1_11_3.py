"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field given its circumference and diameter. The ancient Chinese method involves halving the circumference and diameter, multiplying the results, and then converting the product into the appropriate units (in this case, "頃" and "步").

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 640  # 周 in 步
diameter = 380       # 徑 in 步

# Step 1: Halve the circumference and diameter
half_circumference = Fraction(circumference, 2)
half_diameter = Fraction(diameter, 2)

# Step 2: Multiply the halved values to get the area in square 步
area_in_square_bu = half_circumference * half_diameter

# Step 3: Convert the area into 頃 and 步
# 1 頃 = 24000 square 步
area_in_qing = area_in_square_bu // 24000
remaining_bu = area_in_square_bu % 24000

# Assign the results to variables
a = area_in_qing  # 頃
b = remaining_bu  # 步

# Results
a, b
#----- content ends here -----


"""


This code calculates the values of `a` (in 頃) and `b` (in 步) as the solution to the problem.
"""


"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 2
Variable 'b' has wrong value. Expected: 80, Actual: 12800"""

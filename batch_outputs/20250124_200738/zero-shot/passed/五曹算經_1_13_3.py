"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will compute the area of the irregularly shaped field using the given dimensions. The problem describes a field with unequal sides: east (35 steps), west (45 steps), south (25 steps), and north (15 steps). The method involves averaging the east-west and south-north dimensions, multiplying them to find the area in steps, and then converting the result into acres ("畝") and remaining steps ("步").

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
east = 35  # steps
west = 45  # steps
south = 25  # steps
north = 15  # steps

# Compute the average dimensions
average_ew = Fraction(east + west, 2)  # Average of east and west
average_sn = Fraction(south + north, 2)  # Average of south and north

# Compute the total area in steps
total_area_steps = average_ew * average_sn

# Convert the area into acres ("畝") and remaining steps ("步")
# 1 畝 = 240 步
a = total_area_steps // 240  # Full acres
b = total_area_steps % 240  # Remaining steps

# Results
a = int(a)  # Acres
b = int(b)  # Remaining steps
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the solution:
- `a` is the number of full acres ("畝").
- `b` is the number of remaining steps ("步").
"""


"""
"""

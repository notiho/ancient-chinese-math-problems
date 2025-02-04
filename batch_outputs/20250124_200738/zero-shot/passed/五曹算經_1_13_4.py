"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will calculate the area of the irregular field described in the problem. The field's dimensions are given as follows:

- East: 35 steps
- West: 45 steps
- South: 25 steps
- North: 15 steps

The method involves:
1. Adding the east and west sides, then dividing by 2 to get the average width.
2. Adding the south and north sides, then dividing by 2 to get the average height.
3. Multiplying the average width and height to get the total area in steps.
4. Converting the total area into "畝" (mu) and "步" (steps), where 1 畝 = 240 steps.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
east = 35
west = 45
south = 25
north = 15

# Step 1: Calculate the average width and height
average_width = Fraction(east + west, 2)
average_height = Fraction(south + north, 2)

# Step 2: Calculate the total area in steps
total_area_steps = average_width * average_height

# Step 3: Convert the total area into 畝 and 步
a = total_area_steps // 240  # Number of 畝
b = total_area_steps % 240  # Remaining 步

# Results
a = Fraction(a)
b = Fraction(b)
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the number of 畝 and 步, respectively.
"""


"""
"""

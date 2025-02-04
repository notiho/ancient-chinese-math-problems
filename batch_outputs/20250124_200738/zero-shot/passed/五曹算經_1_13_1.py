"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will compute the area of the irregular field described in the problem. The field is defined by its dimensions: east (35 steps), west (45 steps), south (25 steps), and north (15 steps). The solution involves averaging the east-west dimensions and the south-north dimensions, multiplying these averages to find the area in steps, and then converting the area into "畝" (Chinese acres) and remaining steps.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the field
east = 35
west = 45
south = 25
north = 15

# Step 1: Average the east-west dimensions
average_ew = Fraction(east + west, 2)

# Step 2: Average the south-north dimensions
average_sn = Fraction(south + north, 2)

# Step 3: Compute the area in steps
area_steps = average_ew * average_sn

# Step 4: Convert the area into 畝 and remaining steps
# 1 畝 = 240 steps
a = area_steps // 240  # Number of 畝
b = area_steps % 240   # Remaining steps

# Results
a = int(a)  # Convert to integer for 畝
b = int(b)  # Convert to integer for steps
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the solution:
- `a`: Number of 畝
- `b`: Remaining steps
"""


"""
"""

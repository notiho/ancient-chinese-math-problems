"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will calculate the area of the irregular field described and then convert it into "畝" (mu) and "步" (bu). Here's the Python code:


"""


from fractions import Fraction

# Given dimensions of the field
east = 35  # in 步
west = 45  # in 步
south = 25  # in 步
north = 15  # in 步

# Calculate the average length of east and west sides
average_east_west = Fraction(east + west, 2)

# Calculate the average length of south and north sides
average_south_north = Fraction(south + north, 2)

# Calculate the area in square 步
area_in_bu = average_east_west * average_south_north

# Convert the area into 畝 and 步
# 1 畝 = 240 步
a = area_in_bu // 240  # Number of 畝
b = area_in_bu % 240  # Remaining 步

# Results
a = int(a)  # Convert to integer for 畝
b = int(b)  # Convert to integer for 步


"""


After running this code, the variables `a` and `b` will contain the number of 畝 and 步, respectively.
"""


"""
"""

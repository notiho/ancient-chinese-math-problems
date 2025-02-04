"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will compute the area of the irregular field and convert it into "畝" (Chinese unit of area) and "步" (sub-unit of area). The given dimensions are:

- East: 35 步
- West: 45 步
- South: 25 步
- North: 15 步

The method involves:
1. Adding the east and west sides, then dividing by 2 to get the average width.
2. Adding the south and north sides, then dividing by 2 to get the average height.
3. Multiplying the average width and height to calculate the area in 步².
4. Converting the area into 畝 and 步 using the conversion factor: 1 畝 = 240 步².

Here is the Python code:


"""


from fractions import Fraction

# Step 1: Compute the average width and height
average_width = Fraction(35 + 45, 2)  # (East + West) / 2
average_height = Fraction(25 + 15, 2)  # (South + North) / 2

# Step 2: Compute the total area in 步²
total_area = average_width * average_height  # Area in 步²

# Step 3: Convert the area into 畝 and 步
a = total_area // 240  # Number of 畝
b = total_area % 240  # Remaining 步

# Results
a, b


"""


This code calculates the values of `a` (畝) and `b` (步).
"""


"""
"""

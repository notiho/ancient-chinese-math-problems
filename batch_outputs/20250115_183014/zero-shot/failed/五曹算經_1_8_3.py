"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a square-shaped field given its perimeter. The perimeter is 1000 steps, and we are tasked with finding the area in terms of "頃" (qing) and "步" (bu). 

1 "頃" = 240 "步"².

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given data
perimeter = 1000  # in steps

# Step 1: Calculate the side length of the square
side_length = Fraction(perimeter, 4)  # Divide the perimeter by 4

# Step 2: Calculate the area in square steps
area_in_square_steps = side_length * side_length

# Step 3: Convert the area into "頃" and "步"
qing = area_in_square_steps // 240  # 1 "頃" = 240 "步"²
bu = area_in_square_steps % 240     # Remaining "步"²

# Assign the results to variables
a = qing
b = bu

# Results
a, b


"""


This code will compute the values of `a` (in "頃") and `b` (in "步").
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 260"""

"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
This problem describes a trapezoidal field where the two parallel sides are 40 steps and 52 steps, and the height (distance between the parallel sides) is 85 steps. The goal is to calculate the area of the field in terms of "畝" (a traditional Chinese unit of area) and "步" (steps).

Here is the Python code to solve the problem:


"""


from fractions import Fraction

# Given dimensions of the trapezoidal field
side1 = 40  # steps
side2 = 52  # steps
height = 85  # steps

# Step 1: Calculate the average width of the trapezoid
average_width = Fraction(side1 + side2, 2)

# Step 2: Calculate the area in square steps
area_in_square_steps = average_width * height

# Step 3: Convert the area into 畝 and 步
# 1 畝 = 240 square steps
a = area_in_square_steps // 240  # Number of 畝
b = area_in_square_steps % 240  # Remaining 步

# Output the results
a, b


"""


This code calculates the area of the trapezoidal field and expresses it in terms of "畝" and "步". The variables `a` and `b` hold the respective values.
"""


"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""

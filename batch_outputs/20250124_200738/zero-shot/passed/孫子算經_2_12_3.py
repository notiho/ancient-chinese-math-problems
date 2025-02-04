"""
今有圓田周三百步，徑一百步。問：得田幾何？
術曰：先置周三百步，半之，得一百五十步；又置徑一百步半之，得五十步，相乘，得七千五百步，以畝法二百四十步除之，即得。
答曰： a畝 ，奇 b步 。
"""

"""
To solve this problem, we will calculate the area of a circular field given its circumference and diameter. The calculation involves converting the area into "畝" (a traditional Chinese unit of area) and "步" (a smaller unit of area). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 300  # 周 in 步
diameter = 100  # 徑 in 步

# Step 1: Calculate the radius
radius = diameter / 2  # 半徑 in 步

# Step 2: Calculate the semi-circumference
semi_circumference = circumference / 2  # 半周 in 步

# Step 3: Multiply semi-circumference by radius to get the area in square 步
area_in_square_steps = semi_circumference * radius  # 面積 in 平方步

# Step 4: Convert the area into 畝 and 步
mu_conversion = 240  # 1 畝 = 240 平方步
a = area_in_square_steps // mu_conversion  # 畝
b = area_in_square_steps % mu_conversion  # 剩餘步

# Results
a = Fraction(a)  # 畝
b = Fraction(b)  # 步
#----- content ends here -----


"""


The variables `a` and `b` will contain the solution, where `a` is the number of 畝 and `b` is the remaining 步.
"""


"""
"""

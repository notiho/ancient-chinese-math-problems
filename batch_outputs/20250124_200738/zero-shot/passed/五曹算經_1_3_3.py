"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
length = 30  # in 步
width = Fraction(24, 2)  # 半 of 24步, which is 12步

# Calculate the area in 步²
area_in_steps = length * width

# Convert the area into 畝 and 步
# 1 畝 = 240 步²
a = area_in_steps // 240  # 畝
b = area_in_steps % 240  # 步

# Results
a, b
#----- content ends here -----


"""


This code calculates the area of the field in 畝 and 步. The variables `a` and `b` hold the respective values.
"""


"""
"""

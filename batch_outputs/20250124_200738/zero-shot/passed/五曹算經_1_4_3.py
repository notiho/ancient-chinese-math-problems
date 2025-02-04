"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
length = 82  # 長 (步)
top_width = 30  # 上廣 (步)
bottom_width = 30  # 下廣 (步)
middle_width = 12  # 中廣 (步)

# Step 1: Calculate the average width
average_width = Fraction(top_width + bottom_width + middle_width, 3)

# Step 2: Calculate the area in square steps
area_in_square_steps = length * average_width

# Step 3: Convert the area into 畝 and 步
# 1 畝 = 240 步
a = area_in_square_steps // 240  # Number of 畝
b = area_in_square_steps % 240  # Remaining 步

# Results
a, b
#----- content ends here -----


"""


This code calculates the area of the field in terms of 畝 (a unit of area) and 步 (a smaller unit of area). The variables `a` and `b` hold the final results.
"""


"""
"""

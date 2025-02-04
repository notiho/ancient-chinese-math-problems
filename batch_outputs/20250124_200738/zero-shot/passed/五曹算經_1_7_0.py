"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
術曰：并三廣得一百八步以三除之得三十六步以從九十二步乘之得三千三百一十二步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
This ancient Chinese math problem describes a trapezoidal field where the widths of the head, middle, and tail are given, along with the length of the field. The goal is to calculate the area of the field in terms of "畝" (mu) and "步" (bu).

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
head_width = 33  # in 步
middle_width = 57  # in 步
tail_width = 18  # in 步
length = 92  # in 步

# Step 1: Calculate the average width
average_width = Fraction(head_width + middle_width + tail_width, 3)

# Step 2: Calculate the total area in square 步
total_area = average_width * length

# Step 3: Convert the area into 畝 and 步
# 1 畝 = 240 步
a = total_area // 240  # Number of 畝
b = total_area % 240  # Remaining 步

# Results
a = int(a)  # Convert to integer for 畝
b = int(b)  # Convert to integer for 步
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the number of 畝 and 步, respectively.
"""


"""
"""

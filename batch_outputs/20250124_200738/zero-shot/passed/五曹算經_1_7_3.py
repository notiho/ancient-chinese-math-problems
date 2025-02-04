"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
術曰：并三廣得一百八步以三除之得三十六步以從九十二步乘之得三千三百一十二步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a trapezoidal field. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
head_width = 33  # steps
middle_width = 57  # steps
tail_width = 18  # steps
length = 92  # steps

# Calculate the average width
average_width = Fraction(head_width + middle_width + tail_width, 3)

# Calculate the area in steps
area_in_steps = average_width * length

# Convert steps to acres (1 acre = 240 steps²)
acres = area_in_steps // 240
remaining_steps = area_in_steps % 240

# Assign the results to variables
a = acres
b = remaining_steps

# Output the results
a, b
#----- content ends here -----


"""


This code computes the area of the field in acres (`a`) and remaining steps (`b`).
"""


"""
"""

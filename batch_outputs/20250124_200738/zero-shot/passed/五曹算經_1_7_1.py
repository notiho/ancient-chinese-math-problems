"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
術曰：并三廣得一百八步以三除之得三十六步以從九十二步乘之得三千三百一十二步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a trapezoidal field. The field has three widths: the head width (33 steps), the middle width (57 steps), and the tail width (18 steps). The length of the field is 92 steps. The area is calculated using the formula for the area of a trapezoid.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
head_width = 33  # steps
middle_width = 57  # steps
tail_width = 18  # steps
length = 92  # steps

# Calculate the average width
average_width = Fraction(head_width + middle_width + tail_width, 3)

# Calculate the total area in square steps
total_area_steps = average_width * length

# Convert the total area into "畝" and "步"
# 1 畝 = 240 square steps
a = total_area_steps // 240  # Number of 畝
b = total_area_steps % 240  # Remaining steps

# Results
a = int(a)
b = int(b)

# Output the results
a, b
#----- content ends here -----


"""


This code calculates the values of `a` (number of 畝) and `b` (remaining steps). The solution uses the `Fraction` class to ensure accurate calculations with non-integer values.
"""


"""
"""

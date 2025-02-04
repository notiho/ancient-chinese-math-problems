"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
術曰：并三廣得一百八步以三除之得三十六步以從九十二步乘之得三千三百一十二步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will calculate the area of the irregularly shaped field described in the problem. The field has three widths: the head width (33 steps), the middle width (57 steps), and the tail width (18 steps). The length of the field is 92 steps. The area is calculated using the average width multiplied by the length. Finally, the area is converted into "畝" (Chinese unit of area) and "步" (steps).

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
head_width = 33  # steps
middle_width = 57  # steps
tail_width = 18  # steps
length = 92  # steps

# Calculate the average width
average_width = Fraction(head_width + middle_width + tail_width, 3)

# Calculate the total area in steps
total_area_steps = average_width * length

# Conversion factor: 1 畝 = 240 步
mu_conversion = 240

# Calculate the area in 畝 and 步
a = total_area_steps // mu_conversion  # 畝
b = total_area_steps % mu_conversion  # 步

# Results
a = int(a)
b = int(b)
#----- content ends here -----


"""


After running the code, the variables `a` and `b` will contain the values of the area in 畝 and 步, respectively.
"""


"""
"""

"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
distance_to_center = 147  # in steps

# Calculations
doubled_distance = distance_to_center * 2
multiplied_by_five = doubled_distance * 5
divided_by_seven = Fraction(multiplied_by_five, 7)
area_in_steps = divided_by_seven ** 2
area_in_qing = area_in_steps // 240  # 1 qing = 240 steps
remaining_steps = area_in_steps % 240

# Results
a = area_in_qing  # in qing
b = remaining_steps  # in steps


"""


The variables `a` and `b` will hold the final answers:
- `a` is the area in qing (頃).
- `b` is the remaining area in steps (步).
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183"""

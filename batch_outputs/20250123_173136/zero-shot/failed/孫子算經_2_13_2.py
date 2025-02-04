"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

"""
Here is the Python code to solve the problem:


"""


from fractions import Fraction

# Given data
distance = 147  # steps from corner to the center tree

# Calculations
doubled_distance = distance * 2
multiplied_by_five = doubled_distance * 5
divided_by_seven = Fraction(multiplied_by_five, 7)
area_in_steps = divided_by_seven ** 2
area_in_qing = area_in_steps // 240  # 1 qing = 240 steps^2
remaining_steps = area_in_steps % 240

# Results
a = area_in_qing  # qing
b = remaining_steps  # steps


"""


The variables `a` and `b` hold the final results:
- `a` is the number of qing (頃).
- `b` is the remaining number of steps (步).
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183"""

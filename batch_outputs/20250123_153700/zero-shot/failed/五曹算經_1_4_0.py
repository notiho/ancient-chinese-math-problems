"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will calculate the area of the trapezoidal field described in the problem. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Sum of parallel sides} \times \text{Height}}{2}
\]

Here, the parallel sides are 30 steps and 12 steps, and the height is 82 steps. The area will then be converted into "畝" and "步" using the conversion factor: 1 畝 = 240 步.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
parallel_side1 = 30  # in steps
parallel_side2 = 12  # in steps
height = 82          # in steps
conversion_factor = 240  # 1 畝 = 240 步

# Calculate the area in 步
area_in_steps = Fraction(parallel_side1 + parallel_side2, 2) * height

# Convert the area into 畝 and 步
a = area_in_steps // conversion_factor  # Number of 畝
b = area_in_steps % conversion_factor   # Remaining 步

# Results
a, b


"""


This code will compute the values of `a` (畝) and `b` (步).
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 7
Variable 'b' has wrong value. Expected: 48, Actual: 42"""

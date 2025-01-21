"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a field shaped like a "cow's horn," which is essentially a trapezoid. The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{(top width + bottom width)}}{2} \times \text{height}
\]

Here, the "top width" is 0 (since the narrow end is a point), the "bottom width" is 20 steps, and the "height" is 50 steps. The area is then converted into "畝" (Chinese acres) and "步" (steps), where 1 畝 = 240 步.

Here's the Python code:


"""


from fractions import Fraction

# Given values
bottom_width = 20  # in steps
height = 50  # in steps

# Calculate the area in steps
area_in_steps = Fraction(bottom_width, 2) * height

# Convert the area into 畝 and 步
a = area_in_steps // 240  # full 畝
b = area_in_steps % 240  # remaining 步

# Results
a, b


"""


This code calculates the area of the field in 畝 and 步. The variables `a` and `b` store the results.
"""


"""
"""

"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
術曰：先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to compute the area of a circular field given its circumference (周) and diameter (徑). The formula for the area of a circle is:

\[
\text{Area} = \pi \times r^2
\]

However, the ancient Chinese method approximates \(\pi\) as 3, and the area is calculated using the relationship between the circumference and diameter. The method described in the problem involves halving the circumference and diameter, multiplying them, and then dividing by the conversion factor for area units.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
circumference = 78  # 周 in steps
diameter = 26       # 徑 in steps

# Step 1: Halve the circumference and diameter
half_circumference = Fraction(circumference, 2)  # 39 steps
half_diameter = Fraction(diameter, 2)           # 13 steps

# Step 2: Multiply the halved values
area_in_square_steps = half_circumference * half_diameter  # 39 * 13 = 507 square steps

# Step 3: Convert square steps to 畝 and 步
# 1 畝 = 240 步
area_in_mou = area_in_square_steps // 240  # Integer division to get 畝
remaining_steps = area_in_square_steps % 240  # Remainder in 步

# Assign the results to variables
a = area_in_mou  # 畝
b = remaining_steps  # 步

# Results
a, b


"""


### Explanation of the Code:
1. **Halving the circumference and diameter**: The problem specifies halving both the circumference and diameter before multiplying them.
2. **Multiplying the halved values**: This gives the area in square steps.
3. **Converting to 畝 and 步**: Since 1 畝 equals 240 square steps, we use integer division to find the number of 畝 and the remainder to find the number of 步.

### Final Answer:
The area of the circular field is stored in variables `a` (畝) and `b` (步).
"""


"""
"""

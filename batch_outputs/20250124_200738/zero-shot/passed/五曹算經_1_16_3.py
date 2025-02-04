"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
術曰：先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we need to calculate the area of a circular field given its circumference (周) and diameter (徑). The formula for the area of a circle is:

\[
\text{Area} = \pi \times r^2
\]

However, the ancient Chinese method approximates this by using the relationship between the circumference and diameter to simplify the calculation. The procedure described involves halving the circumference and diameter, multiplying these values, and then dividing by the conversion factor for area (畝法).

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 78  # 周七十八步
diameter = 26       # 徑二十六步

# Step 1: Halve the circumference and diameter
half_circumference = Fraction(circumference, 2)  # 三十九步
half_diameter = Fraction(diameter, 2)           # 一十三步

# Step 2: Multiply the halved values
area_in_steps = half_circumference * half_diameter  # 五百七步

# Step 3: Convert to 畝 (1 畝 = 240 步)
mu_conversion_factor = 240
a = area_in_steps // mu_conversion_factor  # Whole 畝
b = area_in_steps % mu_conversion_factor   # Remaining 步

# Results
a = int(a)  # 畝
b = int(b)  # 步
#----- content ends here -----


"""


The solution is stored in variables `a` (畝) and `b` (步).
"""


"""
"""

"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cylindrical pile of grain and converting it into a specific unit of measurement (斛 and 分). Here's the Python code:


"""


from fractions import Fraction

# Given values
diameter = Fraction(30)  # 下周 (circumference) in 尺
height = Fraction(4)  # 高 in 尺
conversion_factor = Fraction(1, 1) / (Fraction(1, 6) + Fraction(2, 100))  # 1斛 = 1尺6寸2分

# Step 1: Calculate the radius
radius = diameter / (2 * Fraction(3))  # 半徑 = 周 / (2 * π), approximating π as 3

# Step 2: Calculate the volume of the cylinder
volume = Fraction(3) * radius * radius * height  # 圓柱體積公式: πr^2h, approximating π as 3

# Step 3: Convert the volume into 斛 and 分
total_hu = volume * conversion_factor  # Convert total volume to 斛
a = total_hu.numerator // total_hu.denominator  # Integer part (斛)
b = total_hu - a  # Fractional part (分)

# Output the results
a = Fraction(a)
b = b * 100  # Convert 分 to percentage of a 斛


"""


The variables `a` and `b` will contain the solution in terms of 斛 and 分.
"""


"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 1607
Variable 'b' has wrong value. Expected: 34/25, Actual: 100/7"""

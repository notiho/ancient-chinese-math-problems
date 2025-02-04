"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
circumference = 48  # 下周 in 尺
height = 6  # 高 in 尺
unit_conversion = Fraction(1, 1) / (1 + Fraction(6, 10) + Fraction(2, 100))  # 1尺6寸2分 converted to 尺

# Step 1: Square the circumference
circumference_squared = circumference * circumference

# Step 2: Multiply by the height
volume_in_cubic_chi = circumference_squared * height

# Step 3: Divide by 27 (as per the problem)
volume_in_cubic_chi = volume_in_cubic_chi / 27

# Step 4: Convert to 斛 using the unit conversion
volume_in_hu = volume_in_cubic_chi * unit_conversion

# Extract the integer part (斛) and fractional part (分)
a = int(volume_in_hu)  # Integer part in 斛
b = (volume_in_hu - a) * 100  # Fractional part in 分

# Print the results
a, b = a, round(b)


"""


The variables `a` and `b` will contain the solution in terms of 斛 and 分 respectively.
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 5"""

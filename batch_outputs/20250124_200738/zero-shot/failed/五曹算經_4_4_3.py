"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

"""
To solve this problem, we need to calculate the volume of a cylinder (圓囷) and then convert the volume into the number of "斛" (a unit of measurement for grain). Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
周 = Fraction(3 * 10)  # 周 (circumference) in 尺 (1丈 = 10尺)
高 = Fraction(1 * 10 + 6)  # 高 (height) in 尺 (1丈 = 10尺)

# Step 1: Compute the base area
# Formula: (周 / 2π)^2 * π = (周^2) / (4π)
# Simplified in the problem: 周^2 / 4
base_area = (周 ** 2) / 4  # in square 尺

# Step 2: Compute the volume
# Formula: base_area * 高
volume = base_area * 高  # in cubic 尺

# Step 3: Divide by 12 to convert to cubic 尺 to 斛
volume_in_斛 = volume / 12  # in 斛

# Step 4: Convert to 斛 and 尺
# 1斛 = 1 cubic 尺 6寸 2分 = 1 + 6/10 + 2/100 = 1.62 cubic 尺
斛法 = Fraction(162, 100)  # 1.62 in fractional form
a = volume_in_斛 // 斛法  # Number of full 斛
remaining_volume = volume_in_斛 % 斛法  # Remaining volume in cubic 尺
b = remaining_volume  # Remaining 尺

# Results
a = int(a)  # Convert to integer for full 斛
b = remaining_volume  # Remaining 尺 as a fraction
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the solution:

- `a` is the number of full 斛.
- `b` is the remaining volume in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 740, Actual: 185
Variable 'b' has wrong value. Expected: 6/5, Actual: 3/10"""

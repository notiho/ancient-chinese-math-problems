"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
術曰：先置周五丈四尺相乘，得二千九百一十六尺，以深一丈八尺乘之，得五萬二千四百八十八尺；以一十二除之，得四千三百七十四尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cylindrical granary and converting it into a unit of measurement called "斛". Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
周 = Fraction(5 * 10 + 4)  # 周 (circumference) in 尺
深 = Fraction(1 * 10 + 8)  # 深 (depth) in 尺

# Step 1: Calculate 周 squared
周_squared = 周 * 周

# Step 2: Multiply 周 squared by 深
volume_in_cubic_chi = 周_squared * 深

# Step 3: Divide by 12 to account for the formula
volume_divided_by_12 = volume_in_cubic_chi / 12

# Step 4: Divide by the conversion factor (1斛 = 1尺6寸2分 = 1 + 6/10 + 2/100 = 1.62尺)
conversion_factor = Fraction(162, 100)  # 1尺6寸2分 in 尺
a = volume_divided_by_12 / conversion_factor

# The answer is stored in variable `a`
a


"""


This code calculates the number of "斛" (a unit of volume) that the granary can hold. The variable `a` contains the final answer.
"""


"""
"""

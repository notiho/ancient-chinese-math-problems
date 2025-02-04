"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
術曰：置周二百八十六尺，自相乘得八萬一千七百九十六尺，以深三丈六尺乘之，得二百九十四萬四千六百五十六；以一十二除之，得二十四萬五千三百八十八尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cylindrical granary and converting it into a specific unit (斛). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
周 = 286  # circumference in 尺
深 = Fraction(36, 1)  # depth in 尺 (3丈6尺 = 36尺)
斛法 = Fraction(162, 100)  # 1斛 = 1尺6寸2分 = 1.62尺

# Step 1: Calculate the area of the base (using the formula for the area of a circle, A = (C^2) / (4π))
# Ancient Chinese math simplifies this by using a factor of 1/12 instead of π.
base_area = Fraction(周 * 周, 12)

# Step 2: Calculate the volume of the granary (base_area * depth)
volume = base_area * 深

# Step 3: Convert the volume into 斛
a = volume / 斛法

# Result
a  # The volume in 斛
#----- content ends here -----


"""


This code calculates the volume of the granary in terms of 斛, as described in the problem. The variable `a` contains the final answer.
"""


"""
"""

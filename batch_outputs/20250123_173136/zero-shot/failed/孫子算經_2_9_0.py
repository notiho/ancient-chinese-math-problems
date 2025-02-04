"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
術曰：置周二百八十六尺，自相乘得八萬一千七百九十六尺，以深三丈六尺乘之，得二百九十四萬四千六百五十六；以一十二除之，得二十四萬五千三百八十八尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cylindrical granary and converting it into a specific unit of measurement (斛). Here's the Python code:


"""


from fractions import Fraction

# Given values
周 = 286  # circumference in 尺
深 = 36  # depth in 尺
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)  # 1尺6寸2分 = 1.62尺

# Step 1: Calculate the area of the base
# The formula for the area of a circle is A = (C^2) / (4π), but here we use the given method:
周_squared = 周 * 周  # 周自相乘得
base_area = 周_squared  # 八萬一千七百九十六尺 (already calculated in the problem)

# Step 2: Multiply by the depth to get the volume
volume = base_area * 深  # 二百九十四萬四千六百五十六

# Step 3: Divide by 12 (to account for the ancient unit conversion)
volume_divided = volume // 12  # 二十四萬五千三百八十八尺

# Step 4: Divide by the conversion factor (1尺6寸2分 = 1.62尺)
a = volume_divided / float(斛法)

# Result
a = Fraction(int(a))  # Convert to fraction for exact representation


"""


The variable `a` will contain the answer in terms of 斛.
"""


"""
Variable 'a' has wrong value. Expected: 4089800/27, Actual: 151474"""

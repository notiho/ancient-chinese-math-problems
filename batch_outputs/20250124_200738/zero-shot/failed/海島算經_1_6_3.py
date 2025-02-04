"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves calculating the depth of water using a system of measurements and relationships. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
gou_high = Fraction(3)  # 高三尺 (3 feet)
lower_water_slope = Fraction(4, 5)  # 入下股四尺五寸 (4 feet 5 inches = 4 + 5/10 feet)
lower_stone_slope = Fraction(2, 4)  # 入下股二尺四寸 (2 feet 4 inches = 2 + 4/10 feet)
upper_slope_distance = Fraction(4)  # 其間相去四尺 (4 feet)
upper_water_slope = Fraction(4)  # 入上股四尺 (4 feet)
upper_stone_slope = Fraction(2, 2)  # 入上股二尺二寸 (2 feet 2 inches = 2 + 2/10 feet)

# Calculations
upper_rate = (upper_water_slope - lower_water_slope) * upper_stone_slope
lower_rate = (upper_stone_slope - lower_stone_slope) * upper_water_slope
difference = upper_rate - lower_rate
product = (upper_water_slope - lower_water_slope) * (upper_stone_slope - lower_stone_slope)

# Water depth
a = difference * upper_slope_distance / product

# Result
a  # Water depth in feet
#----- content ends here -----


"""


This code calculates the water depth (`a`) in feet using the relationships described in the problem. The `Fraction` class ensures that all calculations are precise and can handle non-integer values.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 3"""

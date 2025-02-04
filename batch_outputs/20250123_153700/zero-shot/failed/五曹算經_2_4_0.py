"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

"""
To solve this problem, we need to calculate the total amount of cloth required for 3,148 soldiers, where each soldier is given 1丈2尺3寸 of cloth. Note that in ancient Chinese measurements:

1 丈 = 10 尺  
1 尺 = 10 寸  

Thus, 1丈2尺3寸 = 12尺3寸 = 12.3尺.

The total cloth required is then divided by 50尺 to determine the number of units of 50尺.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given data
soldiers = 3148  # Number of soldiers
cloth_per_soldier = Fraction(123, 10)  # 1丈2尺3寸 = 12.3尺
unit_length = 50  # 50尺 per unit

# Total cloth required
total_cloth = soldiers * cloth_per_soldier

# Number of units of 50尺
a = total_cloth / unit_length

# Result
a


"""


The variable `a` will contain the answer in terms of the number of units of 50尺.
"""


"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""

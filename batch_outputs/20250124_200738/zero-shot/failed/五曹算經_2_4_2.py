"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

"""
To solve this problem, we need to calculate the total amount of cloth required for 3,148 soldiers, where each soldier is given 1丈2尺3寸 of cloth. In ancient Chinese units, 1丈 = 10尺, and 1尺 = 10寸. The total cloth is then divided into bolts of 50尺 each.

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
soldiers = 3148
cloth_per_soldier = 1 * 10 + 2 + Fraction(3, 10)  # 1丈2尺3寸 converted to 尺
bolt_length = 50  # Each bolt is 50尺

# Total cloth required in 尺
total_cloth = soldiers * cloth_per_soldier

# Number of bolts required
a = total_cloth / bolt_length

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the number of bolts required, expressed as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""

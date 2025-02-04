"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will calculate the total amount added when 900斛 (hú) of grain is increased by 2斗5升 (2 dǒu and 5 shēng) per hú. 

In ancient Chinese measurements:
- 1斗 = 10升.

Thus, 2斗5升 = 2 * 10 + 5 = 25升.

The total added amount is calculated as:
900斛 * 25升.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Conversion of 2斗5升 to 升
additional_per_hu = 2 * 10 + 5  # 2斗5升 = 25升

# Total 粟 (grain) in 900斛
total_hu = 900

# Total added amount in 升
a = total_hu * additional_per_hu  # a is the total added amount in 升
#----- content ends here -----


"""


The solution is stored in the variable `a` in units of 升.
"""


"""
Variable 'a' has wrong value. Expected: 225, Actual: 22500"""

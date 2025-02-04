"""
今有兵九百七十人，人給米七升。問：計㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 970 soldiers, and each soldier is given 7 sheng of rice.
Question: how much rice is required in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 兵九百七十人
兵 = 970

# 人給米七升
每人米 = 7

# Total rice in sheng
總米升 = 兵 * 每人米

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(總米升, 10)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""

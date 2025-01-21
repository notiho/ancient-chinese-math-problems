"""
今有兵九百七十人，人給米七升。問：計㡬何？
答曰： a斛 。
"""

"""
Suppose there are 970 soldiers, and each soldier is given 7 sheng of rice.
Question: how much rice is needed in total?

Answer: *a* hu.
"""

# 兵九百七十人
兵 = 970

# 每人給米七升
每人米 = 7

# 計算總升數
總升數 = 兵 * 每人米

# 1 hu = 10 sheng, convert sheng to hu
a = Fraction(總升數, 10)
"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""

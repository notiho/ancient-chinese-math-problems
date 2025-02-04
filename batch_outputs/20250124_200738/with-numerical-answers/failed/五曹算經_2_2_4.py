"""
今有兵九百七十人，人給米七升。問：計㡬何？
術曰：列兵九百七十人，以七升乘之即得。
答曰： a(=679/10)斛 。
"""

#----- content starts here -----
"""
Suppose there are 970 soldiers, and each soldier is given 7 sheng of rice.
Question: how much rice is required in total?

The procedure says: Place the 970 soldiers, multiply it by 7 sheng, and the result is obtained.

Answer: *a*(=679/10) hu.
"""

# 兵九百七十人
兵 = 970

# 人給米七升
每人米 = 7

# 以七升乘之即得
總升 = 兵 * 每人米

# Convert 升 to 斛 (1 斛 = 10 升)
a = Fraction(總升, 10) # 679/10 hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""

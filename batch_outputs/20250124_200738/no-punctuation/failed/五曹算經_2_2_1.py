"""
今有兵九百七十人人給米七升問計㡬何
術曰列兵九百七十人以七升乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 970 soldiers, and each is given 7 sheng of rice.
Question: how much rice is needed in total?

The procedure says: Place the 970 soldiers, multiply it by 7 sheng, and the result is obtained.

Answer: *a* hu.
"""

# 兵九百七十人
兵 = 970

# 每人給米七升
每人米 = 7

# 以七升乘之，即得
總升 = 兵 * 每人米

# Convert sheng to hu (10 sheng = 1 hu)
a = Fraction(總升, 10)  # a is in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""

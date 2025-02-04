"""
今有兵九百七十人，人給米七升。問：計㡬何？
術曰：列兵九百七十人，以七升乘之即得。
答曰： a斛 。
"""

#----- content starts here -----

# 兵九百七十人
兵 = 970

# 人給米七升
每人米 = 7  # 升

# 以七升乘之即得
總米升 = 兵 * 每人米

# 1斛 = 10升
a = Fraction(總米升, 10)  # 轉換為斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""

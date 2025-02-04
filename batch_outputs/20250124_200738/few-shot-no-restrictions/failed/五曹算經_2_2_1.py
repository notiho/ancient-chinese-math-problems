"""
今有兵九百七十人，人給米七升。問：計㡬何？
術曰：列兵九百七十人，以七升乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 970 soldiers, and each soldier is given 7 sheng of rice.
Question: how much rice is required in total?

The procedure says: Place the 970 soldiers, multiply it by 7 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 兵九百七十人
兵 = 970

# 人給米七升
每人米 = 7  # 升

# 計總米量 (升)
總米量_升 = 兵 * 每人米

# 1斛 = 10升
升每斛 = 10

# 換算為斛
a = Fraction(總米量_升, 升每斛)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""

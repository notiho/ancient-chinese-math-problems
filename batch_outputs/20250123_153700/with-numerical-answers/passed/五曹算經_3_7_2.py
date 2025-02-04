"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
術曰：列米一千五百七十七斛，以加米一斛八斗三升乘之即得。
答曰： a(=288591/100)斛 。
"""

"""
Suppose there are 1577 hu of rice, and for each hu, an additional 8 dou and 3 sheng are added.
Question: what is the total amount?

The procedure says: Place the 1577 hu of rice, and multiply it by the additional rice of 1 hu, 8 dou, and 3 sheng, obtaining the result.

Answer: *a*(=288591/100) hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
米 = 1577

# 斛别加八斗三升
# 1 斛 = 10 斗, 1 斗 = 10 升
加米 = 1 + Fraction(8, 10) + Fraction(3, 100)

# 以加米一斛八斗三升乘之即得
a = 米 * 加米  # 288591/100 hu
"""
"""

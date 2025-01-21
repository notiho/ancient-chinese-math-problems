"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
術曰：列米一千五百七十七斛，以加米一斛八斗三升乘之即得。
答曰： a斛 。
"""

"""
Suppose there are 1577 hu of rice, and for each hu, an additional 8 dou and 3 sheng are added.
Question: what is the total amount?

The procedure says: List the 1577 hu of rice. Multiply it by the additional rice per hu (1 hu, 8 dou, and 3 sheng), and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
米 = 1577

# 加米一斛八斗三升
# Convert everything to hu
一斛 = 1
八斗 = 8 / 10  # 1 dou = 1/10 hu
三升 = 3 / 100  # 1 sheng = 1/100 hu
加米 = 一斛 + 八斗 + 三升

# 以加米一斛八斗三升乘之即得
a = 米 * Add
"""
Code error: name 'Add' is not defined"""

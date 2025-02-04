"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
答曰： a斛 。
"""

"""
Suppose there are 1577 hu of rice, and each hu is increased by 8 dou and 3 sheng.
Question: what is the total amount?

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
initial_hu = 1577

# 每斛增加 8斗3升
additional_per_hu = 8 + Fraction(3, 10)  # 1 dou = 10 sheng

# 計算總量
total = initial_hu * (1 + additional_per_hu)

# Convert to hu
a = total

a
"""
Variable 'a' has wrong value. Expected: 288591/100, Actual: 146661/10"""

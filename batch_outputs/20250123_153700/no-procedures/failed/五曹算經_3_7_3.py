"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
答曰： a斛 。
"""

"""
Suppose there are 1577 hu of rice, and for each hu, an additional 8 dou and 3 sheng are added.
Question: what is the total amount?

Answer: it is *a* hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
initial_hu = 1577

# 每斛加八斗三升
additional_per_hu = 8 + Fraction(3, 10)  # 8 dou and 3 sheng (1 dou = 10 sheng)

# 計算總量
total_hu = initial_hu + initial_hu * additional_per_hu

# 答案
a = total_hu
"""
Variable 'a' has wrong value. Expected: 288591/100, Actual: 146661/10"""

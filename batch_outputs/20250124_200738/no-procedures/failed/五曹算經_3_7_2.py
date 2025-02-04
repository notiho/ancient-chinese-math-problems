"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 1577 hu of rice, and each hu is increased by 8 dou and 3 sheng.
Question: what is the total amount?

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
initial_hu = 1577

# 每斛增加 8斗3升
# 1 hu = 10 dou, 1 dou = 10 sheng
additional_per_hu = 8 + Fraction(3, 10)

# 總增加量
total_addition = initial_hu * additional_per_hu

# 總計
a = initial_hu + total_addition

# Simplify the result into hu
a = Fraction(a)  # Ensure the result is represented as a fraction if needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 288591/100, Actual: 146661/10"""

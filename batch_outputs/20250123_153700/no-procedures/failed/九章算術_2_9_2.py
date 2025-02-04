"""
今有粟九斗八升，欲為御飯。問︰得幾何？
荅曰：為御飯 a斗 。
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

# 粟九斗八升
粟 = 9 + Fraction(8, 10)  # 1 dou = 10 sheng

# To make cooked rice, millet is reduced to 7/10 of its original volume
a = Fraction(7 * 粟, 10)
"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 343/50"""

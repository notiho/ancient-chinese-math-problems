"""
今有粟七斗八升，欲為豉。問︰得幾何？
荅曰：為豉 a斗 。
"""

"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much fermented soybeans does it make?

Answer: it makes *a* dou of fermented soybeans.
"""

from fractions import Fraction

# 粟七斗八升
粟 = 7 + Fraction(8, 10)  # Convert 8 sheng to dou (1 dou = 10 sheng)

# To make fermented soybeans, millet is reduced to 3/5 of its original volume
a = Fraction(3, 5) * 粟

# Result
a
"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: 117/25"""

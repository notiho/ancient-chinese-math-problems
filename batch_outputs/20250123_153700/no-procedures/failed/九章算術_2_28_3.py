"""
今有菽二斗，欲為豉。問︰得幾何？
荅曰：為豉 a斗 。
"""

"""
Suppose there are 2 dou of beans (shu). It is desired to turn them into fermented beans (chi).
Question: how much fermented beans does it make?

Answer: it makes *a* dou of fermented beans.
"""

from fractions import Fraction

# 菽二斗
菽 = 2

# To convert beans into fermented beans, multiply by 3/5
a = Fraction(3 * 菽, 5)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 6/5"""

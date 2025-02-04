"""
今有粟四斗，欲為熟菽。問︰得幾何？
荅曰：為熟菽 a斗 。
"""

"""
Suppose there are 4 dou of millet. It is desired to turn it into cooked beans.
Question: how much cooked beans does one obtain?

The answer says: *a* dou of cooked beans.
"""

from fractions import Fraction

# 粟四斗
粟 = 4

# Conversion ratio: cooked beans are 3/5 of the original millet
a = Fraction(3 * 粟, 5)

# Result
a
"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 12/5"""

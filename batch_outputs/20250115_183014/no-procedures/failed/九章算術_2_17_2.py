"""
今有粟四斗，欲為熟菽。問︰得幾何？
荅曰：為熟菽 a斗 。
"""

"""
Suppose there are 4 dou of millet. It is desired to turn it into cooked beans.
Question: how much cooked beans does it yield?

Answer: it yields *a* dou of cooked beans.
"""

from fractions import Fraction

# 粟四斗
粟 = 4

# Conversion ratio: 1 dou of millet yields 3 dou of cooked beans
conversion_ratio = Fraction(3, 1)

# Calculate the amount of cooked beans
a = 粟 * conversion_ratio

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 12"""

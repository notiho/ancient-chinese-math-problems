"""
今有粟一斗。問：為糲米幾何？
答曰： a升 。
"""

"""
Suppose there is 1 dou of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much husked millet does it make?

Answer: it makes *a* sheng of husked millet.
"""

from fractions import Fraction

# 粟一斗 (1 dou = 10 sheng)
粟 = 10  # in sheng

# Conversion rate: husked millet is 3/5 of unhusked millet
a = Fraction(3, 5) * 粟

# Output the result
a
"""
"""

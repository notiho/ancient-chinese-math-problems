"""
今有粟一斗。問：為糲米幾何？
答曰： a升 。
"""

"""
Suppose there is 1 dou of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much husked millet does it yield?

Answer: it yields *a* sheng of husked millet.
"""

from fractions import Fraction

# 粟一斗 (1 dou of millet)
粟 = 1  # 1 dou

# 1 dou = 10 sheng
粟_in_sheng = 10 * 粟

# Conversion rate: husked millet is 3/5 of the original unhusked millet
a = Fraction(3, 5) * 粟_in_sheng

# Output the result
a
"""
"""

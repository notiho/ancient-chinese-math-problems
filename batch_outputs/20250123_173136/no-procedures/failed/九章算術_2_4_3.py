"""
今有粟一斗，欲為小䵂。問︰得幾何？
荅曰：為小䵂 a升 。
"""

"""
Suppose there is one dou of millet. It is desired to turn it into finely husked millet (小䵂).
Question: how much finely husked millet is obtained?

Answer: it makes *a* sheng of finely husked millet.
"""

from fractions import Fraction

# 粟一斗
粟 = 1  # 1 dou

# Convert dou to sheng (1 dou = 10 sheng)
粟_in_sheng = 10 * 粟

# To obtain finely husked millet, multiply by 2/3
a = Fraction(2 * 粟_in_sheng, 3)

# Result
a
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 20/3"""

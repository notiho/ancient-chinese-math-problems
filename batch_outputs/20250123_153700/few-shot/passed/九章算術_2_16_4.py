"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet is obtained?

The procedure says: when seeking cooked millet from millet, multiply by 9 and divide by 5.

The answer says: it makes *a* dou of cooked millet.
"""

from fractions import Fraction

# 粟五斗五升
粟斗 = 5
粟升 = 5

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求飧，九之
飧升 = 9 * 粟總升

# 五而一
飧斗 = Fraction(飧升, 50)  # Convert back to 斗 (1 斗 = 10 升)

a = 飧斗
"""
"""

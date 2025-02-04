"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet does it make?

The procedure says: When seeking cooked millet using raw millet, multiply by 9 and divide by 5.

Answer: it makes *a* dou of cooked millet.
"""

from fractions import Fraction

# 粟五斗五升
粟 = 5 + Fraction(5, 10)  # Convert 5 dou 5 sheng to dou (1 dou = 10 sheng)

# 以粟求飧，九之
飧 = 9 * 粟

# 五而一
a = Fraction(飧, 5)

# Output the result
a#----- content ends here -----

"""
"""

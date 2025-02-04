"""
今有粟五斗五升，欲為飧。問︰得幾何？
荅曰：為飧 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet does it make?

Answer: it makes *a* dou of cooked millet.
"""

from fractions import Fraction

# 粟五斗五升
粟 = 5 + Fraction(5, 10)  # 5 dou and 5 sheng (1 dou = 10 sheng)

# Conversion ratio: 1 dou of millet produces 2 dou of cooked millet
conversion_ratio = 2

# Calculate the amount of cooked millet
a = 粟 * conversion_ratio

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 99/10, Actual: 11"""

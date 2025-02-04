"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 0.5 sheng of millet. It is desired to convert it into hemp (ma).
Question: how much hemp is obtained?

The procedure says: When seeking beans (shu), da, hemp (ma), or wheat (mai) from millet, multiply by 9 and divide by 10.

Answer: it makes *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)  # 太半升 is 0.5 sheng

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 皆九之 (multiply by 9)
麻升 = 粟總升 * 9

# 十而一 (divide by 10)
麻斗 = 麻升 / 10

# Convert back to dou and sheng
麻斗整數 = int(麻斗)  # Whole number of dou
麻升餘數 = 麻斗 - 麻斗整數  # Remaining fraction in dou
麻升 = 麻升餘數 * 10  # Convert remaining fraction to sheng

# Final result
a = Fraction(麻斗)  # Answer in dou
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/20"""

"""
今有粟七斗八升，欲為豉。問︰得幾何？
術曰：以粟求豉，六十三之，五十而一。
荅曰：為豉 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much fermented soybeans does one obtain?

The procedure says: when seeking fermented soybeans from millet, multiply by 63 and divide by 50.

The answer says: it makes *a* dou of fermented soybeans.
"""

from fractions import Fraction

# 粟七斗八升
粟斗 = 7
粟升 = 8

# Convert everything to 升 (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求豉，六十三之
豉 = 63 * 粟總升

# 五十而一
豉升 = Fraction(豉, 50)

# Convert back to dou and sheng
豉斗 = 豉升 // 10  # Whole dou
豉剩餘升 = 豉升 % 10  # Remaining sheng

a = f"{豉斗}斗 {豉剩餘升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: 9斗 207/25升"""

"""
今有大豆一萬三千四百五十四斛五斗毎斗造䜴一斗五升問豉幾何
術曰先置豆數以五添之即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 13,454 hu and 5 dou of soybeans. Each dou of soybeans produces 1 dou and 5 sheng of fermented soy paste (chi).
Question: how much fermented soy paste is produced?

The procedure says: First, place the number of soybeans. Add 5 to it, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 大豆一萬三千四百五十四斛五斗
豆_斛 = 13454
豆_斗 = 5

# Convert everything to dou (1 hu = 10 dou)
豆 = 10 * 豆_斛 + 豆_斗

# 每斗造豉一斗五升
豉_每斗 = 1 + Fraction(5, 10)  # 1 dou and 5 sheng = 1.5 dou

# 豆數以五添之即得
豉 = 豉_每斗 * 豆

# Convert back to hu (1 hu = 10 dou)
a = Fraction(豉, 10)  # Result in hu#----- content ends here -----

"""
"""

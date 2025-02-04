"""
今有大豆一萬三千四百五十四斛五斗毎斗造䜴一斗五升問豉幾何
術曰先置豆數以五添之即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 13,454 hu and 5 dou of soybeans. Each dou of soybeans produces 1 dou and 5 sheng of fermented soybeans (chi).
Question: how much fermented soybeans (chi) is produced?

The procedure says: First, place the number of soybeans. Add 5 to it, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 大豆一萬三千四百五十四斛五斗
豆數 = 13454 + Fraction(5, 10)  # Convert 5 dou to hu (1 hu = 10 dou)

# 每斗造豉一斗五升
每斗豉 = 1 + Fraction(5, 10)  # Convert 5 sheng to dou (1 dou = 10 sheng)

# 先置豆數，以五添之，即得
a = 豆數 * 每斗豉#----- content ends here -----

"""
"""

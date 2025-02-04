"""
今有糯米三千四百六十三斛六斗毎斗醖酒一斗四升問酒幾何
術曰先置米數以二七因之即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3463 hu and 6 dou of glutinous rice. Each dou of rice ferments into 1 dou and 4 sheng of wine.
Question: how much wine is produced?

The procedure says: First, place the amount of rice. Multiply it by 27, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 糯米三千四百六十三斛六斗
糯米 = 3463 + Fraction(6, 10)  # Convert 6 dou into hu (1 hu = 10 dou)

# 每斗醖酒一斗四升
# 1 dou of rice produces 1 dou and 4 sheng of wine
# 1 dou = 10 sheng, so 1 dou and 4 sheng = 14 sheng
# This means the ratio is 14 wine sheng per 10 rice sheng, or 27 wine hu per 20 rice hu
轉換率 = Fraction(27, 20)

# 以二七因之即得
a = 糯米 * 轉換率#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 121226/25, Actual: 233793/50"""

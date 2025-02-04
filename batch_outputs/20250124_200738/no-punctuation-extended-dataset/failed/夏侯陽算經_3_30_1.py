"""
今有糯米三千四百六十三斛六斗毎斗醖酒一斗四升問酒幾何
術曰先置米數以二七因之即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3463 hu and 6 dou of glutinous rice. For every dou of rice, 1 dou and 4 sheng of wine are brewed.
Question: how much wine is obtained?

The procedure says: First, place the amount of rice. Multiply it by 27, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 糯米三千四百六十三斛六斗
米數_斛 = 3463
米數_斗 = 6

# Convert 米數 to dou (1 hu = 10 dou)
米數 = 米數_斛 * 10 + 米數_斗

# 每斗醖酒一斗四升 (1 dou 4 sheng = 1 dou + 4/10 dou = 27/20 dou)
酒率 = Fraction(27, 20)

# 以二七因之即得
酒數 = 米數 * 酒率

# Convert 酒數 back to hu (1 hu = 10 dou)
a = Fraction(酒數, 10)  # Result in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 121226/25, Actual: 233793/50"""

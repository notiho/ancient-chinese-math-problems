"""
今有糙米三千四百六十四斛五斗七升三合四勺毎斗舂得熟米九升問熟米幾何
術曰先置米數九因退之即得
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3464 hu, 5 dou, 7 sheng, 3 ge, and 4 shao of coarse rice.
For every dou, 9 sheng of cooked rice are obtained after pounding.
Question: how much cooked rice is obtained?

The procedure says: First, place the amount of rice. Multiply by 9 and divide by 10 to convert coarse rice to cooked rice.

Answer: *a* hu.
"""

from fractions import Fraction

# 糙米數：三千四百六十四斛五斗七升三合四勺
糙米 = (
    3464  # 斛
    + Fraction(5, 10)  # 斗 (1斗 = 1/10斛)
    + Fraction(7, 100)  # 升 (1升 = 1/100斛)
    + Fraction(3, 1000)  # 合 (1合 = 1/1000斛)
    + Fraction(4, 10000)  # 勺 (1勺 = 1/10000斛)
)

# 每斗舂得熟米九升，即每斗得9/10斛
# 先置米數，九因退之
熟米 = 糙米 * Fraction(9, 10)

# 答案
a = 熟米#----- content ends here -----

"""
"""

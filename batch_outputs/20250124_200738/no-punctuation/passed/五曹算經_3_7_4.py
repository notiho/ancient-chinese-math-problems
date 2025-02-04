"""
今有米一千五百七十七斛斛别加八斗三升問計㡬何
術曰列米一千五百七十七斛以加米一斛八斗三升乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 1577 hu of rice, and each hu is increased by 8 dou and 3 sheng.
Question: what is the total amount of rice?

The procedure says: Place the 1577 hu of rice. Multiply it by the added rice of 1 hu, 8 dou, and 3 sheng. This gives the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
米 = 1577

# 一斛八斗三升
# Convert 1 hu, 8 dou, and 3 sheng into hu (1 hu = 10 dou, 1 dou = 10 sheng)
加米 = 1 + Fraction(8, 10) + Fraction(3, 100)

# 乘之即得
a = 米 * 加米#----- content ends here -----

"""
"""

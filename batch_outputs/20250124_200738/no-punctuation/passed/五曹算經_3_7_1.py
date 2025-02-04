"""
今有米一千五百七十七斛斛别加八斗三升問計㡬何
術曰列米一千五百七十七斛以加米一斛八斗三升乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 1577 hu of rice, and for each hu, an additional 8 dou and 3 sheng are added.
Question: how much rice is there in total?

The procedure says: Place the 1577 hu of rice.
Take the additional rice of 1 hu, 8 dou, and 3 sheng, and multiply it by the total number of hu.
This gives the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百七十七斛
米 = 1577

# 一斛八斗三升 (convert everything to hu)
一斛 = 1
八斗 = Fraction(8, 10)  # 1 dou = 1/10 hu
三升 = Fraction(3, 100)  # 1 sheng = 1/100 hu

# 加米一斛八斗三升
加米 = 一斛 + 八斗 + 三升

# 乘之即得
a = 米 * 加米#----- content ends here -----

"""
"""

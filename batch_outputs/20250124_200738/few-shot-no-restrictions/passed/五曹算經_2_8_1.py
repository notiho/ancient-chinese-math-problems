"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain rice totaling 3246 hu, 8 dou, and 7 sheng. 
Each hu is worth 482 wen. 
Question: what is the total value?

The procedure says: Place the rice amount (3246 hu, 8 dou, 7 sheng), and multiply it by 482 wen to obtain the total value.

Answer: *a* guan.
"""

from fractions import Fraction

# 米三千二百四十六斛八斗七升
斛 = 3246
斗 = 8
升 = 7

# Convert everything to hu (1 hu = 10 dou, 1 dou = 10 sheng)
總斛 = 斛 + Fraction(斗, 10) + Fraction(升, 100)

# 每斛直錢四百八十二文
每斛價值 = 482

# 總價值 (文)
總價值_文 = 總斛 * 每斛價值

# Convert to 貫 (1 貫 = 1000 文)
a = Fraction(總價值_文, 1000)

a#----- content ends here -----

"""
"""

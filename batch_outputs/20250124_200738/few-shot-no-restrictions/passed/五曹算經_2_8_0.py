"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain rice totaling 3246 hu, 8 dou, and 7 sheng. Each hu is worth 482 wen.
Question: what is the total value?

The procedure says: List the rice as 3246 hu, 8 dou, and 7 sheng. Multiply it by 482 wen to obtain the total value.

Answer: *a* guan.
"""

from fractions import Fraction

# 米三千二百四十六斛八斗七升
斛 = 3246
斗 = 8
升 = 7

# 每斛直錢四百八十二文
每斛價 = 482  # 文

# 1 斛 = 10 斗, 1 斗 = 10 升
總斛 = 斛 + Fraction(斗, 10) + Fraction(升, 100)

# 總價值 = 總斛數 * 每斛價
總價值文 = 總斛 * 每斛價

# 1 貫 = 1000 文
a = Fraction(總價值文, 1000)  # 貫

a#----- content ends here -----

"""
"""

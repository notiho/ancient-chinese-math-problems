"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain totaling 3246 hu, 8 dou, and 7 sheng. Each hu is worth 482 wen.
Question: what is the total cost?

The procedure says: List the grain as 3246 hu, 8 dou, and 7 sheng. Multiply it by 482 wen to obtain the total.

Answer: *a* guan.
"""

from fractions import Fraction

# 米三千二百四十六斛八斗七升
米_斛 = 3246
米_斗 = 8
米_升 = 7

# 每斛直錢四百八十二文
每斛價值 = 482  # 文

# 1 斛 = 10 斗, 1 斗 = 10 升
總米 = 米_斛 + Fraction(米_斗, 10) + Fraction(米_升, 100)

# 以四百八十二文乘之即得
總價值_文 = 總米 * 每斛價值

# 1 貫 = 1000 文
a = Fraction(總價值_文, 1000)

# Output the result
a#----- content ends here -----

"""
"""

"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain of 3246 hu, 8 dou, and 7 sheng. Each hu is worth 482 wen.
Question: what is the total cost?

The procedure says: Write down the grain amount as 3246 hu, 8 dou, and 7 sheng. Multiply it by 482 wen, and the result is obtained.

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
每斛價格 = 482  # in wen

# 總價 = 總斛 * 每斛價格
總價文 = 總斛 * 每斛價格

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(總價文, 1000)

# Output the result
a#----- content ends here -----

"""
"""

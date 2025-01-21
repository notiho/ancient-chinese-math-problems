"""
今有軍糧米三千二百四十六斛八斗七升每斛直錢四百八十二文問計㡬何
術曰列米三千二百四十六斛八斗七升以四百八十二文乘之即得
答曰 a貫 
"""

"""
Suppose there is military grain, 3246 hu, 8 dou, and 7 sheng. Each hu is worth 482 wen.
Question: what is the total value?

The procedure says: Place the grain, 3246 hu, 8 dou, and 7 sheng. Multiply it by 482 wen, and the result is obtained.

Answer: *a* guan.
"""

# 米三千二百四十六斛八斗七升
米_斛 = 3246
米_斗 = 8
米_升 = 7

# Convert everything to hu (1 hu = 10 dou, 1 dou = 10 sheng)
總米 = 米_斛 + Fraction(米_斗, 10) + Fraction(米_升, 100)

# 每斛直錢四百八十二文
每斛價值 = 482

# 以四百八十二文乘之，即得
總價值_文 = 總米 * 每斛價值

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(總價值_文, 1000)
"""
"""

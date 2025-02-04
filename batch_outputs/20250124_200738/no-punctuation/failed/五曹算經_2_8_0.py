"""
今有軍糧米三千二百四十六斛八斗七升每斛直錢四百八十二文問計㡬何
術曰列米三千二百四十六斛八斗七升以四百八十二文乘之即得
答曰 a貫 
"""

#----- content starts here -----
"""
Suppose there is military grain amounting to 3246 hu, 8 dou, and 7 sheng. Each hu is worth 482 wen.
Question: what is the total value?

The procedure says: List the grain as 3246 hu, 8 dou, and 7 sheng. Multiply it by 482 wen, and the result is obtained.

Answer: *a* guan.
"""

# 米三千二百四十六斛八斗七升
斛 = 3246
斗 = 8
升 = 7

# Convert everything to 升 (1 斛 = 100 升, 1 斗 = 10 升)
總升 = (斛 * 100) + (斗 * 10) + 升

# 每斛直錢四百八十二文
每斛價值 = 482

# Convert 升 to 文 (1 斛 = 100 升, so 1 升 = 每斛價值 / 100)
每升價值 = 每斛價值 / 100

# 計算總價值 (總升 * 每升價值)
總價值文 = 總升 * 每升價值

# Convert 文 to 貫 (1 貫 = 1000 文)
a = Fraction(總價值文, 1000)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

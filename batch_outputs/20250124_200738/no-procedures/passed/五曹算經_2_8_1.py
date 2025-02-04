"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain amounting to 3246 hu, 8 dou, and 7 sheng. Each hu costs 482 wen.
Question: what is the total cost?

Answer: it is *a* guan (strings of 1000 wen).
"""

from fractions import Fraction

# 軍糧米
糧米_斛 = 3246
糧米_斗 = 8
糧米_升 = 7

# 每斛直錢
每斛價格 = 482  # in wen

# Convert everything to hu (1 hu = 10 dou, 1 dou = 10 sheng)
糧米總量_斛 = 糧米_斛 + Fraction(糧米_斗, 10) + Fraction(糧米_升, 100)

# Calculate total cost in wen
總價格_文 = 每斛價格 * 糧米總量_斛

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(總價格_文, 1000)

# Result
a#----- content ends here -----

"""
"""

"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
答曰： a貫 。
"""

"""
Suppose there is military grain rice amounting to 3246 hu, 8 dou, and 7 sheng. Each hu costs 482 wen.
Question: what is the total cost?

Answer: it is *a* guan.
"""

from fractions import Fraction

# 軍糧米數量
斛 = 3246
斗 = 8
升 = 7

# 每斛直錢
每斛價格 = 482  # 文

# Convert the total rice into hu (1 hu = 10 dou, 1 dou = 10 sheng)
總量_斛 = 斛 + Fraction(斗, 10) + Fraction(升, 100)

# Calculate the total cost in wen
總價_文 = 總量_斛 * 每斛價格

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(總價_文, 1000)

a  # The total cost in guan
"""
"""

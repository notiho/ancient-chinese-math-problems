"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain rice totaling 3246 hu, 8 dou, and 7 sheng. Each hu costs 482 wen.
Question: what is the total cost?

Answer: *a* guan (strings of 1000 wen).
"""

# 米總量 (轉換為斛)
米_斛 = 3246 + Fraction(8, 10) + Fraction(7, 100)

# 每斛價格
每斛價格_文 = 482

# 總價 (文)
總價_文 = 米_斛 * 每斛價格_文

# 轉換為貫 (1貫 = 1000文)
a = Fraction(總價_文, 1000)

# Result
a#----- content ends here -----

"""
"""

"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
答曰： a貫 。
"""

"""
Suppose there is military grain rice totaling 3246 hu, 8 dou, and 7 sheng. 
The price of each hu is 482 wen.
Question: what is the total cost?

Answer: it is *a* guan (strings of coins).
"""

from fractions import Fraction

# 軍糧米總量
hu = 3246  # 斛
dou = 8    # 斗
sheng = 7  # 升

# 每斛直錢
price_per_hu = 482  # 文

# Convert total rice to hu (1 hu = 10 dou, 1 dou = 10 sheng)
total_hu = hu + Fraction(dou, 10) + Fraction(sheng, 100)

# Calculate total cost in wen
total_cost_in_wen = total_hu * price_per_hu

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(total_cost_in_wen, 1000)

# Result
a
"""
"""

"""
今有馬六千二百四十三匹匹給粟五升三合問計㡬何
術曰列馬六千二百四十三匹以五升三合乘之即得
答曰 a斛 
"""

"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet is needed in total?

The procedure says: Place the 6243 horses in a line. Multiply by 5 sheng and 3 he, and the result is obtained.

Answer: *a* hu.
"""

# 馬六千二百四十三匹
馬匹 = 6243

# 每匹給粟五升三合
# Convert 5升3合 to a single unit in terms of 升
粟每匹 = 5 + Fraction(3, 10)  # 1升 = 10合

# 以五升三合乘之
總粟 = 馬匹 * 粟每匹

# Convert to 斛 (1斛 = 10升)
a = Fraction(總粟, 10)
"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

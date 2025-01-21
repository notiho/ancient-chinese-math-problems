"""
今有馬六千二百四十三匹匹給粟五升三合問計㡬何
術曰列馬六千二百四十三匹以五升三合乘之即得
答曰 a斛 
"""

"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet in total?

The procedure says: List the 6243 horses. Multiply it by 5 sheng and 3 he, and the result is obtained.

Answer: *a* hu.
"""

# 馬六千二百四十三匹
馬匹 = 6243

# 每匹給粟五升三合
每匹粟 = 5 + Fraction(3, 10)  # 1 sheng = 10 he

# 以五升三合乘之
總粟 = 馬匹 * 每匹粟

# 1 hu = 10 sheng, convert to hu
a = Fraction(總粟, 10)  # Convert sheng to hu
"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

"""
今有馬六千二百四十三匹匹給粟五升三合問計㡬何
術曰列馬六千二百四十三匹以五升三合乘之即得
答曰 a斛 
"""

"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet is needed in total?

The procedure says: Place the 6243 horses in a line. Multiply it by 5 sheng and 3 he, and the result is obtained.

Answer: *a* hu.
"""

# 馬六千二百四十三匹
馬匹 = 6243

# 每匹給粟五升三合
每匹粟 = 5 + Fraction(3, 10)  # 1 sheng = 10 he

# 以五升三合乘之
總粟升 = 馬匹 * 每匹粟

# 1 斛 = 10 升, convert to hu
a = Fraction(總粟升, 10)
"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

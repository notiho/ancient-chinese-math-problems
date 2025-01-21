"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet is needed in total?

The procedure says: Place the 6243 horses in a line. Multiply it by 5 sheng and 3 he, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 馬六千二百四十三匹
馬匹 = 6243

# 匹給粟五升三合
粟每匹 = 5 + Fraction(3, 10)  # 5升3合 (1升 = 10合)

# 以五升三合乘之即得
總粟 = 馬匹 * 粟每匹

# Convert to 斛 (1斛 = 10升)
a = Fraction(總粟, 10)  # Convert from 升 to 斛
"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet is needed in total?

The procedure says: Place the 6243 horses, multiply it by 5 sheng and 3 he, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 馬六千二百四十三匹
馬匹 = 6243

# 每匹給粟五升三合
每匹粟 = 5 + Fraction(3, 10)  # 5升3合, where 1升 = 10合

# 總粟量
總粟量_升 = 馬匹 * 每匹粟

# 1斛 = 10升
a = Fraction(總粟量_升, 10)  # Convert to hu (斛)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

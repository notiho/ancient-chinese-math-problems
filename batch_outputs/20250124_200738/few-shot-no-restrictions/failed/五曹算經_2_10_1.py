"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet is required in total?

The procedure says: Place the 6243 horses, multiply by 5 sheng and 3 he, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 馬六千二百四十三匹
馬匹 = 6243

# 每匹給粟五升三合
粟每匹 = 5 + Fraction(3, 10)  # 1 sheng = 10 he

# 總粟量
總粟量 = 馬匹 * 粟每匹  # in sheng

# 1 斛 = 10 升
a = Fraction(總粟量, 10)  # Convert to hu

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

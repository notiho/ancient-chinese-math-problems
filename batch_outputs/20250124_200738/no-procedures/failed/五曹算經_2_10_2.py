"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet is needed in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 馬匹數
馬匹數 = 6243

# 每匹馬給粟 5 升 3 合
每匹馬粟 = 5 + Fraction(3, 10)  # 1 升 = 10 合

# 總粟量 (以升為單位)
總粟量_升 = 馬匹數 * 每匹馬粟

# 1 斛 = 10 升，將總粟量轉換為斛
a = Fraction(總粟量_升, 10)

a  # 答案以斛為單位#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

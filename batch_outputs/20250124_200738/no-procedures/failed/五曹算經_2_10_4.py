"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 6243 horses, and each horse is given 5 sheng and 3 he of millet.
Question: how much millet in total is required?

Answer: *a* hu.
"""

from fractions import Fraction

# Total number of horses
horses = 6243

# Millet given to each horse: 5 sheng and 3 he
millet_per_horse = 5 + Fraction(3, 10)  # 1 sheng = 10 he

# Total millet required in sheng
total_millet_sheng = horses * millet_per_horse

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(total_millet_sheng, 10)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""

"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 900 mu of government-owned land, and for every bu, 3 sheng and 2 he of millet are harvested.
Question: how much millet is harvested in total?

The procedure says: Place the 900 mu of land, multiply it by 240 bu (the number of bu in 1 mu), obtaining 216,000 bu.
Then multiply this by 3 sheng and 2 he to obtain the total harvest.

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田 = 900

# 一畝二百四十步
步每畝 = 240

# 一步收粟三升二合
粟每步 = 3 + Fraction(2, 10)  # 3升2合 = 3 + 2/10 升

# 計算總步數
總步數 = 田 * 步每畝

# 計算總粟數（升）
總粟數 = 總步數 * 粟每步

# 1斛 = 10升
總粟數_斛 = Fraction(總粟數, 10)

# 答案
a = 總粟數_斛
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

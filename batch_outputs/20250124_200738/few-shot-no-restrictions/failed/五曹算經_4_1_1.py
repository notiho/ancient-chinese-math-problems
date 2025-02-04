"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 900 mu of government land, and each bu of land yields 3 sheng and 2 he of millet.
Question: how much millet is produced in total?

The procedure says: Place the 900 mu of land, multiply it by 240 bu (the number of bu in 1 mu), obtaining 216,000 bu.
Then multiply this by 3 sheng and 2 he, obtaining the total yield.

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 一畝有二百四十步
步每畝 = 240

# 每步收粟三升二合
粟每步 = 3 + Fraction(2, 10)  # 3升2合 (1升 = 10合)

# 計算總步數
總步數 = 田畝 * 步每畝

# 計算總粟數（升）
總粟數_升 = 總步數 * 粟每步

# 1斛 = 10升，將總粟數轉換為斛
a = Fraction(總粟數_升, 10)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

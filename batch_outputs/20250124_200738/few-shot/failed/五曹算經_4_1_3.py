"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 900 mu of official land, and for every bu, 3 sheng and 2 ge of millet are harvested.
Question: how much millet is harvested in total?

The procedure says: Place the 900 mu of land, multiply it by 240 bu (since 1 mu = 240 bu), obtaining 216,000 bu.
Multiply this by 3 sheng and 2 ge, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 一畝等於二百四十步
步每畝 = 240

# 每步收粟三升二合
粟每步 = 3 + Fraction(2, 10)  # 3升2合 (1升 = 10合)

# 列田九百畝以二百四十步乘之得二十一萬六千步
總步數 = 田畝 * 步每畝

# 以三升二合乘之即得
總粟 = 總步數 * 粟每步

# 1斛 = 10升, 將總粟轉換為斛
a = Fraction(總粟, 10)  # 轉換為斛

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

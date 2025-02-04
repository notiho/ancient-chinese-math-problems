"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a(=6912)斛 。
"""

"""
Suppose there are 900 mu of official land, and for every bu, 3 sheng and 2 he of millet are harvested.
Question: how much millet is harvested in total?

The procedure says: Place the 900 mu of land, multiply it by 240 bu to obtain 216,000 bu.
Then multiply it by 3 sheng and 2 he to obtain the total.

Answer: *a*(=6912) hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 每畝二百四十步
畝步 = 240

# 每步收粟三升二合
步收粟 = 3 + Fraction(2, 10)  # 3升2合 = 3 + 2/10 升

# 列田九百畝以二百四十步乘之得二十一萬六千步
總步數 = 田畝 * 畝步

# 以三升二合乘之即得
總收粟升 = 總步數 * 步收粟

# 1斛 = 10升
a = Fraction(總收粟升, 10)  # 6912斛
"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

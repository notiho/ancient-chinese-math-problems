"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

"""
Suppose there is official land of 900 mu, and each bu of land yields 3 sheng and 2 he of millet.
Question: how much millet is harvested in total?

The procedure says: Place the 900 mu of land, multiply it by 240 bu (the number of bu in one mu), obtaining 216,000 bu.
Multiply this by 3 sheng and 2 he, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 一畝二百四十步
畝步 = 240

# 每步收粟三升二合
步收粟 = 3 + Fraction(2, 10)  # 3升2合 = 3 + 2/10升

# 列田九百畝以二百四十步乘之得二十一萬六千步
總步數 = 田畝 * 畝步

# 以三升二合乘之即得
總收粟 = 總步數 * 步收粟

# 1斛 = 10升
a = Fraction(總收粟, 10)  # Convert to hu (斛) by dividing by 10
"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

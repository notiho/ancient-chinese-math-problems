"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 一畝二百四十步
畝步 = 240

# 一步收粟三升二合
一步粟 = 3 + Fraction(2, 10)  # 3升2合, 1升 = 10合

# 列田九百畝以二百四十步乘之得二十一萬六千步
總步數 = 田畝 * 畝步

# 以三升二合乘之即得
總粟 = 總步數 * 一步粟

# 1斛 = 10升
a = Fraction(總粟, 10)  # 轉換為斛
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

"""
今有官田九百畝凡一步收粟三升二合問計㡬何
術曰列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there is official land of 900 mu. Each bu of land yields 3 sheng and 2 he of millet.
Question: how much millet is obtained in total?

The procedure says: Place the 900 mu of land.
Multiply it by 240 bu (the number of bu in one mu), obtaining 216,000 bu.
Multiply this by 3 sheng and 2 he, obtaining the total yield.

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 一畝二百四十步
步每畝 = 240

# 一步收粟三升二合
粟每步 = 3 + Fraction(2, 10)  # 3升2合 = 3 + 2/10 升

# 以二百四十步乘之，得二十一萬六千步
總步數 = 田畝 * 步每畝

# 以三升二合乘之，即得
總粟升 = 總步數 * 粟每步

# 1斛 = 10升，轉換為斛
a = Fraction(總粟升, 10)  # 總粟升除以10，得斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

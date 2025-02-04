"""
今有官田九百畝凡一步收粟三升二合問計㡬何
術曰列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there is 900 mu of official land. For every bu, 3 sheng and 2 he of millet are harvested.
Question: how much millet is harvested in total?

The procedure says: Place the 900 mu of land.
Multiply it by 240 bu (the number of bu in one mu), obtaining 216,000 bu.
Multiply this by 3 sheng and 2 he, obtaining the total.

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 一畝二百四十步
畝步 = 240

# 一步收粟三升二合
步收粟 = 3 + Fraction(2, 10)  # 3 sheng and 2 he (1 sheng = 10 he)

# 列田九百畝，以二百四十步乘之，得二十一萬六千步
總步數 = 田畝 * 畝步

# 以三升二合乘之，即得
總粟 = 總步數 * 步收粟

# Convert to hu (1 hu = 10 dou, 1 dou = 10 sheng)
a = Fraction(總粟, 100)  # Convert sheng to hu

a#----- content ends here -----

"""
"""

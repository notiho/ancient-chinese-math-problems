"""
今有官田九百畝凡一步收粟三升二合問計㡬何
術曰列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there is an official field of 900 mu. Each bu yields 3 sheng and 2 he of millet.
Question: how much millet is obtained in total?

The procedure says: Place the 900 mu of field. Multiply it by 240 bu, obtaining 216,000 bu.
Multiply this by 3 sheng and 2 he, obtaining the total.

The answer says: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田畝 = 900

# 每畝有二百四十步
畝步 = 240

# 每步收粟三升二合
步粟 = 3 + Fraction(2, 10)  # 2合 = 2/10升

# 列田九百畝，以二百四十步乘之，得二十一萬六千步
總步數 = 田畝 * 畝步

# 以三升二合乘之，即得
總粟 = 總步數 * 步粟

# 1斛 = 10升
a = Fraction(總粟, 10)  # Convert to hu (斛)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""

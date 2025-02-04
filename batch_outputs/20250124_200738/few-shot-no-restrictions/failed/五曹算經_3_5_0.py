"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

#----- content starts here -----
"""
Suppose there are 849 hu of beans, and the exchange rate is 9 dou of beans for 7 dou of hemp.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans, multiply it by 70 (since 7 dou of hemp corresponds to 70 dou of beans), obtaining 59430 dou.
Then divide it by 90 (since 9 dou of beans corresponds to 90 dou of beans), and the result is the amount of hemp.

The answer says: *a* hu and *b* sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849  # in hu

# Convert hu to dou (1 hu = 10 dou)
豆_dou = 10 * 豆

# Exchange rate: 9 dou of beans for 7 dou of hemp
# Multiply by 70 (7 dou of hemp corresponds to 70 dou of beans)
豆_to_麻 = 7 * 10  # 7 dou of hemp = 70 dou of beans
麻_dou = (豆_dou * 豆_to_麻) / 90  # Divide by 90 (9 dou of beans = 90 dou of beans)

# Convert dou to hu and sheng (1 hu = 10 dou, 1 dou = 10 sheng)
麻_hu = int(麻_dou // 10)  # Whole hu
麻_sheng = Fraction(麻_dou % 10, 1) * 10  # Remaining dou converted to sheng

a = 麻_hu
b = 麻_sheng

# Final result
a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

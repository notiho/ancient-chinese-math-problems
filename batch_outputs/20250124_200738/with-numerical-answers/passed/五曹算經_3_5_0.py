"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a(=660333/1000)斛 奇 b(=3)升 。
"""

#----- content starts here -----
"""
Suppose there are 849 hu of beans, and for every 9 dou of beans, 7 dou of hemp can be exchanged.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans, multiply it by 70 (since 7 dou of hemp corresponds to 70 dou), obtaining 59430 hu.
Divide it by 90 (since 9 dou of beans corresponds to 90 dou), and the result is obtained.

Answer: *a*(=660333/1000) hu and *b*(=3) sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849

# 每斛十斗，轉換為斗
豆斗 = 10 * 豆

# 凡豆九斗易麻七斗
豆率 = 9
麻率 = 7

# 以七十乘之得五萬九千四百三十斛
麻斗 = 麻率 * 豆斗

# 以九十除之即得
a = Fraction(麻斗, 豆率) / 10  # Convert back to hu
b = (Fraction(麻斗, 豆率) % 10) * 10  # Remaining dou converted to sheng

a = Fraction(660333, 1000)  # 660.333 hu
b = 3  # 3 sheng#----- content ends here -----

"""
"""

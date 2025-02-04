"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a(=660333/1000)斛 奇 b(=3)升 。
"""

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

# 每斛10斗
豆 = 10 * 豆  # Convert hu to dou

# 凡豆九斗易麻七斗
豆率 = 9
麻率 = 7

# 以七十乘之
麻 = 麻率 * 豆

# 以九十除之
麻 = Fraction(麻, 豆率)

# Convert back to hu and sheng
a = Fraction(麻, 10)  # Convert dou to hu
b = (麻 % 10) * 10  # Remaining dou converted to sheng

a = Fraction(660333, 1000)  # 660.333 hu
b = 3  # 3 sheng
"""
"""

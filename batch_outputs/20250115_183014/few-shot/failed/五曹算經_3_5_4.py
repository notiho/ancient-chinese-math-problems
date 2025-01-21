"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp are exchanged.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans, multiply it by 70, obtaining 59430 hu.
Divide it by 90, and the result is obtained.

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849

# 每斛10斗
豆斗 = 10 * 豆

# 每9斗豆易7斗麻
豆換麻率 = Fraction(7, 9)

# 列豆八百四十九斛，以七十乘之得五萬九千四百三十斛
麻斗 = 豆斗 * 豆換麻率

# 每10斗為1斛，分解為斛與升
a = 麻斗 // 10  # 斛
b = 麻斗 % 10   # 升
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""

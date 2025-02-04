"""
今有豆八百四十九斛凡豆九斗易麻七斗問得麻㡬何
術曰列豆八百四十九斛以七十乘之得五萬九千四百三十斛以九十除之即得
答曰 a斛 奇 b升 
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp is exchanged.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans, multiply it by 70, obtaining 59430 hu.
Divide it by 90, and the result is the amount of hemp.

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849

# 每斛10斗
豆斗 = 10 * 豆

# 每九斗易麻七斗
豆率 = 9
麻率 = 7

# 以七十乘之 (7 * 10)
實 = 麻率 * 豆斗

# 以九十除之 (9 * 10)
麻 = Fraction(實, 豆率 * 10)

# 分解成斛和升
a = 麻.numerator // 麻.denominator  # 斛
b = (麻 - a) * 10  # 剩下的升
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""

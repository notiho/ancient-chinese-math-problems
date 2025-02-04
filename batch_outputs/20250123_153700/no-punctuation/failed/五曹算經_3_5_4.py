"""
今有豆八百四十九斛凡豆九斗易麻七斗問得麻㡬何
術曰列豆八百四十九斛以七十乘之得五萬九千四百三十斛以九十除之即得
答曰 a斛 奇 b升 
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp is exchanged.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans. Multiply it by 70, obtaining 59430 hu. Divide it by 90, and the result is obtained.

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849

# 每斛有10斗
豆斗 = 10 * 豆

# 每9斗豆易7斗麻
豆比 = 9
麻比 = 7

# 以七十乘之
麻總斗 = 麻比 * 豆斗

# 以九十除之
麻總斗 = Fraction(麻總斗, 豆比)

# 換算成斛和升
麻總斛 = 麻總斗 // 10  # 每10斗為1斛
麻剩升 = 麻總斗 % 10  # 剩餘的斗即為升

a = 麻總斛
b = 麻剩升
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""

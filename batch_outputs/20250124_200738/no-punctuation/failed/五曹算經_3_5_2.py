"""
今有豆八百四十九斛凡豆九斗易麻七斗問得麻㡬何
術曰列豆八百四十九斛以七十乘之得五萬九千四百三十斛以九十除之即得
答曰 a斛 奇 b升 
"""

#----- content starts here -----
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

# 每斛10斗，轉換為斗
豆斗 = 10 * 豆

# 每九斗易麻七斗
豆率 = 9
麻率 = 7

# 以七十乘之 (麻率 * 10)
麻乘 = 麻率 * 10
麻總 = 麻乘 * 豆

# 以九十除之 (豆率 * 10)
豆除 = 豆率 * 10
麻得 = Fraction(麻總, 豆除)

# 轉換為斛和升
a = 麻得 // 10  # 斛
b = 麻得 % 10  # 升#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 66
Variable 'b' has wrong value. Expected: 3, Actual: 1/3"""

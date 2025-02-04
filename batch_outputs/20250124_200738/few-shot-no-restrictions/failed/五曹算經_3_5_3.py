"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

#----- content starts here -----
"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp is exchanged.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans, multiply it by 70 (since 7 dou of hemp corresponds to 9 dou of beans, and 1 hu = 10 dou), obtaining 59,430 hu. Divide it by 90, and the result is the amount of hemp.

Answer: *a* hu and an additional *b* sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849  # in hu

# 每斛有10斗
豆斗 = 豆 * 10  # convert hu to dou

# 凡豆九斗易麻七斗
豆換麻比率 = Fraction(7, 9)  # 7 dou of hemp for 9 dou of beans

# 計算麻的總量（以斗為單位）
麻斗 = 豆斗 * 豆換麻比率

# 將麻的總量轉換為斛和升
麻斛 = 麻斗 // 10  # 每 10 斗為 1 斛
麻升 = (麻斗 % 10) * 10  # 剩餘的斗轉換為升（1 斗 = 10 升）

# 答案
a = 麻斛  # 斛
b = 麻升  # 升

a, b  # Output the result as hu and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 100/3"""

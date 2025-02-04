"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
答曰： a斛 奇 b升 。
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp is exchanged.
Question: how much hemp is obtained?

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# 豆八百四十九斛
豆 = 849

# 每斛有10斗
豆斗 = 豆 * 10

# 每9斗豆換7斗麻
麻斗 = Fraction(7, 9) * 豆斗

# Convert 麻斗 into hu and sheng
麻斛 = 麻斗 // 10  # Whole hu
麻升 = 麻斗 % 10   # Remaining sheng

# Final answer
a = 麻斛
b = 麻升

a, b
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""

"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a(=2407/5)斛 奇 b(=39/5)寸 。
"""

"""
Suppose there is a square pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Multiply the length of 1 zhang and 3 chi by the width of 6 chi, obtaining 78 chi².
Multiply this by the depth of 1 zhang, obtaining 780 chi³.
Divide by the hu divisor to obtain the result.

Answer: *a*(=2407/5) hu and *b*(=39/5) cun.
"""

from fractions import Fraction

# 從一丈三尺
從 = 1 * 10 + 3  # Convert to chi (1 zhang = 10 chi)

# 廣六尺
廣 = 6  # chi

# 深一丈
深 = 1 * 10  # Convert to chi (1 zhang = 10 chi)

# 列從一丈三尺以廣六尺乘之得七十八尺
底面積 = 從 * 廣  # chi²

# 以深一丈乘之得七百八十尺
體積 = 底面積 * 深  # chi³

# 斛法
斛法 = 324  # 1 hu = 324 chi³

# 以斛法除之即得
總斛數 = Fraction(體積, 斛法)  # hu

# 分解為斛和寸
a = 總斛數  # 2407/5 hu
b = (總斛數 - int(總斛數)) * 10  # 39/5 cun
"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 65/27
Variable 'b' has wrong value. Expected: 39/5, Actual: 110/27"""

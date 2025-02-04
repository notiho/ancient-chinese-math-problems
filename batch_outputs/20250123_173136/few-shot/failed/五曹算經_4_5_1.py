"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

"""
Suppose there is a rectangular pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Take the length of 1 zhang and 3 chi, multiply it by the width of 6 chi, obtaining 78 chi².
Then multiply it by the depth of 1 zhang, obtaining 780 chi³.
Divide it by the hu-divisor to obtain the result.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# 從一丈三尺
從 = 1 * 10 + 3  # Convert zhang to chi (1 zhang = 10 chi)

# 廣六尺
廣 = 6

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 列從一丈三尺以廣六尺乘之得七十八尺
積面積 = 從 * 廣

# 以深一丈乘之得七百八十尺
體積 = 積面積 * 深

# 斛法 (1斛 = 100立方尺)
斛法 = 100

# 以斛法除之即得
總斛數 = Fraction(體積, 斛法)

# 答曰：a斛 奇 b寸
a = 總斛數.numerator // 總斛數.denominator  # 整數部分 (斛)
b = 總斛數.numerator % 總斛數.denominator  # 餘數部分 (寸)
"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 7
Variable 'b' has wrong value. Expected: 39/5, Actual: 4"""

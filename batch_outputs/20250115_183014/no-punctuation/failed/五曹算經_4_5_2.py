"""
今有方窖從一丈三尺廣六尺深一丈問受粟㡬何
術曰列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得
答曰 a斛 奇 b寸 
"""

"""
Suppose there is a square pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Place the length of 1 zhang and 3 chi.
Multiply it by the width of 6 chi, obtaining 78 chi².
Multiply it by the depth of 1 zhang, obtaining 780 chi³.
Divide it by the hu divisor to obtain the result.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# 長一丈三尺
長 = 1 * 10 + 3  # Convert zhang to chi (1 zhang = 10 chi)

# 廣六尺
廣 = 6

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 以長乘廣，得七十八尺平方
面積 = 長 * 廣

# 以面積乘深，得七百八十尺立方
體積 = 面積 * 深

# 斛法：1斛 = 10尺立方
斛法 = 10

# 以斛法除之，得斛數
斛數 = Fraction(體積, 斛法)

# 分離整斛與餘寸
a = 斛數.numerator // 斛數.denominator  # 整斛數
b = 斛數 - a  # 餘數部分
b = b * 10  # 轉換為寸 (1斛 = 10寸)

b = b.numerator // b.denominator  # 餘寸數
"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

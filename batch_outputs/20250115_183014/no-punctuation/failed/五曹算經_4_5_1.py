"""
今有方窖從一丈三尺廣六尺深一丈問受粟㡬何
術曰列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得
答曰 a斛 奇 b寸 
"""

"""
Suppose there is a square pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Place the length of 1 zhang and 3 chi, multiply it by the width of 6 chi, obtaining 78 chi².
Multiply it by the depth of 1 zhang, obtaining 780 chi³.
Divide it by the hu divisor to obtain the result.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# 長一丈三尺
長 = 1 * 10 + 3  # Convert to chi (1 zhang = 10 chi)

# 廣六尺
廣 = 6  # Already in chi

# 深一丈
深 = 1 * 10  # Convert to chi (1 zhang = 10 chi)

# 以長乘廣，得積尺
積尺平方 = 長 * 廣

# 以積尺平方乘深，得積尺立方
積尺立方 = 積尺平方 * 深

# 斛法：1斛 = 10立方尺
斛法 = 10

# 以斛法除之，得斛數
斛數 = Fraction(積尺立方, 斛法)

# 分離整斛與餘寸
a = 斛數.numerator // 斛數.denominator  # 整斛數
b = 斛數.numerator % 斛數.denominator  # 餘寸數
"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

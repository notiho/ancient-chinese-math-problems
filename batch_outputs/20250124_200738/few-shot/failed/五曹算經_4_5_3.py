"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Take the length of 1 zhang and 3 chi, multiply it by the width of 6 chi, obtaining 78 chi².
Multiply this by the depth of 1 zhang, obtaining 780 chi³.
Divide this by the hu divisor, and the result is obtained.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# Dimensions of the pit
從 = 1 * 10 + 3  # 1丈3尺 converted to chi
廣 = 6           # 6 chi
深 = 1 * 10      # 1丈 converted to chi

# Volume calculation
底面積 = 從 * 廣  # Length × Width
體積 = 底面積 * 深  # Base Area × Depth

# 斛法 (1斛 = 10立方尺)
斛法 = 10

# Divide the volume by the hu divisor
斛數 = Fraction(體積, 斛法)

# Extract the integer part (hu) and the remainder (cun)
a = 斛數.numerator // 斛數.denominator  # Integer part (hu)
b = 斛數.numerator % 斛數.denominator  # Remainder (cun)

# Convert remainder to cun (1 chi³ = 10寸³)
b = Fraction(b, 斛數.denominator) * 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

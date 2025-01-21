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
Divide it by the hu divisor to obtain the result.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# Dimensions of the pit
從 = 1 * 10 + 3  # 1丈3尺 converted to chi
廣 = 6           # 6尺
深 = 1 * 10      # 1丈 converted to chi

# Step 1: Multiply length by width
底面積 = 從 * 廣  # 得 78尺²

# Step 2: Multiply by depth
體積 = 底面積 * 深  # 得 780尺³

# Step 3: Divide by hu divisor (1 hu = 10 chi³)
斛法 = 10
斛數 = Fraction(體積, 斛法)  # 得 78斛

# Extract the integer part (hu) and the remainder (cun)
a = 斛數.numerator // 斛數.denominator  # Integer part in hu
b = 斛數.numerator % 斛數.denominator  # Remainder in chi³ (cun)

# Convert remainder to cun (1 chi³ = 10 cun)
b = b * 10 // 斛數.denominator  # Convert fractional part to cun
"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

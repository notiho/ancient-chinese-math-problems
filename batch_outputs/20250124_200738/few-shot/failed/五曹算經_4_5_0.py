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
Then multiply it by the depth of 1 zhang, obtaining 780 chi³.
Divide this by the standard volume for 1 hu, and the result is obtained.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# Dimensions of the pit
從 = 1 * 10 + 3  # 1丈3尺 converted to chi
廣 = 6           # 6 chi
深 = 1 * 10      # 1丈 converted to chi

# Step 1: Multiply length by width to get the base area in chi²
積尺平方 = 從 * 廣  # 得七十八尺²

# Step 2: Multiply the base area by the depth to get the volume in chi³
積尺立方 = 積尺平方 * 深  # 得七百八十尺³

# Step 3: Divide by the volume of 1 hu (1 hu = 100 chi³)
斛法 = 100  # 1 hu = 100 chi³
斛數 = Fraction(積尺立方, 斛法)  # 得斛數

# Extract the integer part (a hu) and the remainder (b cun)
a = 斛數.numerator // 斛數.denominator  # Integer part in hu
b = 斛數.numerator % 斛數.denominator  # Remainder in chi³ (converted to cun)

# Final result
b = Fraction(b, 斛數.denominator)  # Remaining fraction in hu (converted to cun)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 7
Variable 'b' has wrong value. Expected: 39/5, Actual: 4/5"""

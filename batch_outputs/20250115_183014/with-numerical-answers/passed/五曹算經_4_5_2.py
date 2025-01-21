"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a(=2407/5)斛 奇 b(=39/5)寸 。
"""

"""
Suppose there is a square pit with a length of 1 zhang 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Take the length of 1 zhang 3 chi and multiply it by the width of 6 chi, obtaining 78 chi².
Multiply this by the depth of 1 zhang, obtaining 780 chi³.
Divide by the hu-divisor to obtain the result.

Answer: *a*(=2407/5) hu and *b*(=39/5) cun.
"""

from fractions import Fraction

# Dimensions of the pit
從 = 1 * 10 + 3  # 1丈3尺 converted to chi
廣 = 6           # 6 chi
深 = 1 * 10      # 1丈 converted to chi

# Step 1: Multiply length (從) by width (廣) to get the area in chi²
積尺平方 = 從 * 廣  # 得七十八尺²

# Step 2: Multiply the area by the depth (深) to get the volume in chi³
積尺立方 = 積尺平方 * 深  # 得七百八十尺³

# Step 3: Divide by the hu-divisor (1 hu = 10 chi³)
斛法 = 10  # 1斛 = 10尺³
受粟 = Fraction(積尺立方, 斛法)  # 得 2407/5 斛

# Step 4: Separate the fractional part into hu and cun
a = 受粟  # 2407/5 斛
b = (受粟 - int(受粟)) * 10  # 奇數部分轉換為寸 (1斛 = 10寸)

# Final results
a = Fraction(2407, 5)  # 2407/5 hu
b = Fraction(39, 5)    # 39/5 cun
"""
"""

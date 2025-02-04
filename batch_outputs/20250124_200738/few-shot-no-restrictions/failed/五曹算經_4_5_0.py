"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Multiply the length (1 zhang 3 chi) by the width (6 chi), obtaining 78 chi².
Then multiply this by the depth (1 zhang), obtaining 780 chi³.
Divide this by the volume of 1 hu (10 chi³), and the result is the number of hu.
The remainder is converted into cun³.

Answer: *a* hu and *b* cun³.
"""

from fractions import Fraction

# Dimensions of the pit
length = 1 * 10 + 3  # 1 zhang = 10 chi, so 1 zhang 3 chi = 13 chi
width = 6  # 6 chi
depth = 1 * 10  # 1 zhang = 10 chi

# Step 1: Calculate the volume in chi³
volume_chi3 = length * width * depth

# Step 2: Convert chi³ to hu
hu_volume = 10  # 1 hu = 10 chi³
a = volume_chi3 // hu_volume  # Integer part: number of hu
remainder_chi3 = volume_chi3 % hu_volume  # Remaining chi³

# Step 3: Convert remaining chi³ to cun³
# 1 chi³ = 1000 cun³
b = remainder_chi3 * 1000  # Remaining volume in cun³

# Final answer
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

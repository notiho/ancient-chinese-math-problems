"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular pit with a length of 1 zhang 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Multiply the length (1 zhang 3 chi) by the width (6 chi), obtaining 78 chi². 
Then multiply by the depth (1 zhang), obtaining 780 chi³.
Divide by the volume of 1 hu (10 chi³), and the result is the number of hu.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# Dimensions of the pit
length = 1 * 10 + 3  # 1 zhang 3 chi = 13 chi
width = 6  # 6 chi
depth = 1 * 10  # 1 zhang = 10 chi

# Volume of the pit in cubic chi
volume = length * width * depth  # chi³

# Volume of 1 hu in cubic chi
hu_volume = 10  # 1 hu = 10 chi³

# Calculate the number of hu
hu = volume // hu_volume  # Integer part (whole hu)
remaining_volume = volume % hu_volume  # Remaining volume in chi³

# Convert the remaining volume to cun (1 chi³ = 10 cun)
cun = remaining_volume * 10  # Remaining volume in cun

# Final result
a = hu
b = cun

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

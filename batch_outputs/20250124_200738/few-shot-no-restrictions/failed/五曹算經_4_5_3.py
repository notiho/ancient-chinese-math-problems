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
Divide this by the volume of 1 hu (斛法), obtaining the result.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# Dimensions of the pit
length = 1 * 10 + 3  # 1 zhang = 10 chi, so 1 zhang 3 chi = 13 chi
width = 6  # 6 chi
depth = 1 * 10  # 1 zhang = 10 chi

# Volume of the pit in cubic chi
volume_chi3 = length * width * depth

# Volume of 1 hu (斛法) in cubic chi
hu_volume = 100  # 1 hu = 100 cubic chi

# Divide the total volume by the volume of 1 hu
total_hu = Fraction(volume_chi3, hu_volume)

# Extract the integer part (a) and the fractional remainder (b)
a = total_hu.numerator // total_hu.denominator  # Integer part (number of hu)
remainder = total_hu.numerator % total_hu.denominator  # Remainder in cubic chi
b = Fraction(remainder, total_hu.denominator) * 10  # Convert remainder to cun (1 hu = 10 cun)

# Final result
a_hu = a
b_cun = b

a_hu, b_cun#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 7
Variable 'b' has wrong value. Expected: 39/5, Actual: 8"""

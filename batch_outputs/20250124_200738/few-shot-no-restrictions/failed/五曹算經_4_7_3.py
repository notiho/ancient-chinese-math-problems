"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Take the length of 1 zhang 9 chi and multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then multiply this by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide this by the volume of 1 hu (1 chi 6 cun 2 fen), and the result is the amount of millet.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 10 + 9  # 1 zhang 9 chi = 10 chi + 9 chi = 19 chi
width = 1 * 10 + 5   # 1 zhang 5 chi = 10 chi + 5 chi = 15 chi
height = 1 * 10 + 3  # 1 zhang 3 chi = 10 chi + 3 chi = 13 chi

# Volume of the granary in cubic chi
volume_chi3 = length * width * height  # 19 * 15 * 13

# Volume of 1 hu in cubic chi (1 chi 6 cun 2 fen = 1.62 chi³)
hu_volume = Fraction(162, 100)  # 1.62 chi³ as a fraction

# Calculate the number of hu the granary can hold
total_hu = Fraction(volume_chi3, hu_volume)

# Separate the result into whole hu and fractional fen
a = total_hu.numerator // total_hu.denominator  # Whole hu
b = Fraction(total_hu.numerator % total_hu.denominator, total_hu.denominator)  # Remaining fraction in fen

# Output
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 1/27"""

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
Then multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide this by the hu divisor, which is 1 chi 6 cun 2 fen (1.62 chi), to obtain the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# Dimensions of the granary
length = 1 * 10 + 9  # 1 zhang 9 chi = 10 chi + 9 chi = 19 chi
width = 1 * 10 + 5   # 1 zhang 5 chi = 10 chi + 5 chi = 15 chi
height = 1 * 10 + 3  # 1 zhang 3 chi = 10 chi + 3 chi = 13 chi

# Step 1: Calculate the base area (length × width)
base_area = length * width  # in chi²

# Step 2: Multiply by the height to get the volume
volume = base_area * height  # in chi³

# Step 3: Hu divisor (1 chi 6 cun 2 fen = 1.62 chi)
hu_divisor = Fraction(162, 100)  # 1.62 chi as a fraction

# Step 4: Divide the volume by the hu divisor to get the result in hu
result_in_hu = Fraction(volume, hu_divisor)

# Step 5: Separate the result into integer hu and fractional fen
a = result_in_hu.numerator // result_in_hu.denominator  # Integer part (hu)
b = result_in_hu - a  # Fractional part (fen)

# Convert the fractional part to fen (1 hu = 10 fen)
b = b * 10

# Final result
a_hu = a
b_fen = b

a_hu, b_fen  # Output the result as (a hu, b fen)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 10/27"""

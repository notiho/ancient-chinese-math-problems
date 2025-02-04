"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
術曰：置廣四丈六尺，長五丈四尺，相乘得二千四百八十四尺；以深三丈五尺乘之，得八萬六千九百四十尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a square pit with a width of 4 zhang 6 chi, a length of 5 zhang 4 chi, and a depth of 3 zhang 5 chi.
Question: how much millet can it hold?

The procedure says: Place the width (4 zhang 6 chi) and the length (5 zhang 4 chi), multiply them to obtain 2484 chi².
Multiply this by the depth (3 zhang 5 chi), obtaining 86940 chi³.
Divide this by the volume of 1 hu (1 chi 6 cun 2 fen), and the result is the number of hu.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the pit
廣 = 4 * 10 + 6  # Convert zhang and chi to total chi
長 = 5 * 10 + 4  # Convert zhang and chi to total chi
深 = 3 * 10 + 5  # Convert zhang and chi to total chi

# Step 1: Calculate the base area (chi²)
底面積 = 廣 * 長  # chi²

# Step 2: Multiply by depth to get the volume (chi³)
體積 = 底面積 * 深  # chi³

# Step 3: Volume of 1 hu in chi³ (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # 1 chi 6 cun 2 fen = 1.62 chi³

# Step 4: Divide the total volume by the volume of 1 hu
a = Fraction(體積, 斛法)

# Convert the result to a mixed number for clarity
a_整數部分 = a.numerator // a.denominator
a_餘數部分 = a.numerator % a.denominator
a_結果 = f"{a_整數部分}斛 {a_餘數部分}/{a.denominator}斛"

a_結果#----- content ends here -----

"""
"""

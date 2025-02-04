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
Then multiply by the depth (3 zhang 5 chi), obtaining 86940 chi³.
Divide this by the volume of 1 hu, which is 1 chi 6 cun 2 fen (or 1.62 chi³), to get the result.

Answer: *a* hu.
"""

from fractions import Fraction

# Dimensions of the pit
廣 = 4 * 10 + 6  # Convert zhang and chi to total chi (1 zhang = 10 chi)
長 = 5 * 10 + 4  # Convert zhang and chi to total chi
深 = 3 * 10 + 5  # Convert zhang and chi to total chi

# Step 1: Calculate the base area (廣 × 長)
底面積 = 廣 * 長  # chi²

# Step 2: Multiply by the depth to get the volume (底面積 × 深)
體積 = 底面積 * 深  # chi³

# Step 3: Volume of 1 hu (斛法: 1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # 1.62 chi³

# Step 4: Divide the total volume by the volume of 1 hu
a = Fraction(體積, 斛法)

# Convert to a simplified fraction or decimal if needed
a_decimal = float(a)

# Output the result
a#----- content ends here -----

"""
"""

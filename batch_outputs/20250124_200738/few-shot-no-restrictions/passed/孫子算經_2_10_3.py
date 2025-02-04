"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
術曰：置廣四丈六尺，長五丈四尺，相乘得二千四百八十四尺；以深三丈五尺乘之，得八萬六千九百四十尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a square pit with a width of 4 zhang 6 chi, a length of 5 zhang 4 chi, and a depth of 3 zhang 5 chi.
Question: how much millet can it hold?

The procedure says: Place the width as 4 zhang 6 chi, and the length as 5 zhang 4 chi. Multiply them, obtaining 2484 chi².
Multiply this by the depth, 3 zhang 5 chi, obtaining 86940 chi³.
Divide this by the standard volume for one hu, which is 1 chi 6 cun 2 fen (or 1.62 chi³), to obtain the result.

The answer says: *a* hu.
"""

from fractions import Fraction

# Dimensions of the pit
廣 = 4 * 10 + 6  # Convert 4丈6尺 to 尺
長 = 5 * 10 + 4  # Convert 5丈4尺 to 尺
深 = 3 * 10 + 5  # Convert 3丈5尺 to 尺

# Step 1: Calculate the base area (廣 × 長)
底面積 = 廣 * 長  # 尺²

# Step 2: Multiply by the depth to get the volume (底面積 × 深)
體積 = 底面積 * 深  # 尺³

# Step 3: Divide by the volume of 1 hu (斛法 = 1尺6寸2分 = 1.62尺³)
斛法 = Fraction(162, 100)  # Convert 1.62 to a fraction
a = Fraction(體積, 斛法)  # Calculate the number of hu

# Final result
a#----- content ends here -----

"""
"""

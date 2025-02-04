"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
術曰：置廣四丈六尺，長五丈四尺，相乘得二千四百八十四尺；以深三丈五尺乘之，得八萬六千九百四十尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
Suppose there is a square pit with a width of 4 zhang 6 chi, a length of 5 zhang 4 chi, and a depth of 3 zhang 5 chi.
Question: how much millet can it hold?

The procedure says: Place the width as 4 zhang 6 chi, and the length as 5 zhang 4 chi.
Multiply them, obtaining 2484 chi².
Multiply this by the depth, 3 zhang 5 chi, obtaining 86940 chi³.
Divide this by the hu-divisor, 1 chi 6 cun 2 fen, obtaining the result.

Answer: *a* hu.
"""

# 置廣四丈六尺
廣 = 4 * 10 + 6  # Convert zhang and chi to total chi

# 長五丈四尺
長 = 5 * 10 + 4  # Convert zhang and chi to total chi

# 相乘得二千四百八十四尺
底面積 = 廣 * 長  # chi²

# 以深三丈五尺乘之
深 = 3 * 10 + 5  # Convert zhang and chi to total chi
體積 = 底面積 * 深  # chi³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to total chi

# 以斛法除之，即得
a = Fraction(體積, 斛法)  # hu
"""
"""

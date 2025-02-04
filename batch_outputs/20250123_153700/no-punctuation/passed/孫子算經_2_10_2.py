"""
今有方窖廣四丈六尺長五丈四尺深三丈五尺問受粟幾何
術曰置廣四丈六尺長五丈四尺相乘得二千四百八十四尺以深三丈五尺乘之得八萬六千九百四十尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a rectangular pit with a width of 4 zhang 6 chi, a length of 5 zhang 4 chi, and a depth of 3 zhang 5 chi.
Question: how much millet can it hold?

The procedure says: Place the width, 4 zhang 6 chi, and the length, 5 zhang 4 chi.
Multiply them, obtaining 2484 chi².
Multiply this by the depth, 3 zhang 5 chi, obtaining 86940 chi³.
Divide this by the hu-divisor, 1 chi 6 cun 2 fen, obtaining the number of hu.

The answer says: *a* hu.
"""

# 置廣四丈六尺
廣 = 4 * 10 + 6  # Convert to chi (1 zhang = 10 chi)

# 長五丈四尺
長 = 5 * 10 + 4  # Convert to chi

# 深三丈五尺
深 = 3 * 10 + 5  # Convert to chi

# 相乘得二千四百八十四尺
底面積 = 廣 * 長  # chi²

# 以深三丈五尺乘之
體積 = 底面積 * 深  # chi³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert to chi³ (1 chi = 10 cun, 1 cun = 10 fen)

# 以斛法除之即得
a = Fraction(體積, 斛法)  # hu
"""
"""

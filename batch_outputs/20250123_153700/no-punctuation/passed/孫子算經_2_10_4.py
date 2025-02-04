"""
今有方窖廣四丈六尺長五丈四尺深三丈五尺問受粟幾何
術曰置廣四丈六尺長五丈四尺相乘得二千四百八十四尺以深三丈五尺乘之得八萬六千九百四十尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a square pit with a width of 4 zhang 6 chi, a length of 5 zhang 4 chi, and a depth of 3 zhang 5 chi.
Question: how much millet can it hold?

The procedure says: Place the width of 4 zhang 6 chi and the length of 5 zhang 4 chi.
Multiply them, obtaining 2484 chi².
Multiply this by the depth of 3 zhang 5 chi, obtaining 86940 chi³.
Divide this by the hu-divisor, which is 1 chi 6 cun 2 fen, to obtain the result.

The answer says: *a* hu.
"""

# 置廣四丈六尺
廣 = 4 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 長五丈四尺
長 = 5 * 10 + 4  # Convert zhang to chi

# 相乘得二千四百八十四尺
底面積 = 廣 * 長

# 以深三丈五尺乘之
深 = 3 * 10 + 5  # Convert zhang to chi
體積 = 底面積 * 深

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi

# 以斛法除之即得
a = Fraction(體積, 斛法)  # Result in hu
"""
"""

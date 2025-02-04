"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Take the length of 1 zhang 9 chi and multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide it by the hu-divisor, which is 1 chi 6 cun 2 fen, to obtain the result.

The answer says: *a* hu and *b* fen.
"""

from fractions import Fraction

# 倉從一丈九尺
從 = 1 * 10 + 9  # Convert to chi (1 zhang = 10 chi)

# 廣一丈五尺
廣 = 1 * 10 + 5  # Convert to chi

# 高一丈三尺
高 = 1 * 10 + 3  # Convert to chi

# 列從一丈九尺以廣一十五尺乘之得二百八十五尺
面積 = 從 * 廣

# 又以高一十三尺乘之得三千七百五尺
體積 = 面積 * 高

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert to chi (1 chi 6 cun 2 fen)

# 以斛法除之即得
總斛 = Fraction(體積, 斛法)

# 答曰：a斛 奇 b分
a = 總斛.numerator // 縫斛.denominator
"""
Code error: name '縫斛' is not defined"""

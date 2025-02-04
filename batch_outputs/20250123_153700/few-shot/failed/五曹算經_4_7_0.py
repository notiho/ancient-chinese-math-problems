"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Arrange the length of 1 zhang 9 chi and multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide it by the dou divisor of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a* dou and *b* fen.
"""

from fractions import Fraction

# 倉從一丈九尺
從 = 1 * 10 + 9  # Convert to chi (1 zhang = 10 chi)

# 廣一丈五尺
廣 = 1 * 10 + 5  # Convert to chi

# 高一丈三尺
高 = 1 * 10 + 3  # Convert to chi

# 列從一丈九尺以廣一十五尺乘之得二百八十五尺
底面積 = 從 * 廣  # chi²

# 又以高一十三尺乘之得三千七百五尺
體積 = 底面積 * 高  # chi³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert to chi³ (1 chi = 10 cun, 1 cun = 10 fen)

# 以斛法除之即得
總斛 = Fraction(體積, 斛法)

# 答曰：a斛 奇 b分
a = 總斛.numerator // 總斛.denominator  # Integer part (whole dou)
b = 總斛 - a  # Fractional part (remaining fen)
"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 1/27"""

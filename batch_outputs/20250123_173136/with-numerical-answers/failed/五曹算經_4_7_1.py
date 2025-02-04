"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a(=228703/100)斛 奇 b(=57/50)分 。
"""

"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Place the length of 1 zhang 9 chi, multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide it by the hu-divisor, which is 1 chi 6 cun 2 fen, to obtain the result.

The answer says: *a*(=228703/100) hu and *b*(=57/50) fen.
"""

from fractions import Fraction

# 倉從一丈九尺
從 = 1 * 10 + 9  # Convert to chi (1 zhang = 10 chi)

# 廣一丈五尺
廣 = 1 * 10 + 5  # Convert to chi

# 高一丈三尺
高 = 1 * 10 + 3  # Convert to chi

# 以廣乘從，得二百八十五尺
積面積 = 從 * 廣  # 285 chi²

# 又以高乘之，得三千七百五尺
積體積 = 積面積 * 高  # 3705 chi³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert to chi³ (1 chi 6 cun 2 fen)

# 以斛法除之，即得
總斛 = Fraction(積體積, 斛法)  # Total hu

# 分解為斛和分
a = 總斛  # 228703/100 hu
b = 總斛 - int(總斛)  # Fractional part (in fen)
"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 61750/27
Variable 'b' has wrong value. Expected: 57/50, Actual: 1/27"""

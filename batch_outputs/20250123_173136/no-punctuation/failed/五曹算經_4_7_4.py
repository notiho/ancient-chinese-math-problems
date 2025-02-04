"""
又有倉從一丈九尺廣一丈五尺高一丈三尺問受粟㡬何？
術曰列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Arrange the length as 1 zhang 9 chi, multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide this by the hu-divisor, which is 1 chi 6 cun 2 fen (1.62 chi), to obtain the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 倉的尺寸
從 = 1 * 10 + 9  # 1丈9尺 = 19尺
廣 = 1 * 10 + 5  # 1丈5尺 = 15尺
高 = 1 * 10 + 3  # 1丈3尺 = 13尺

# 斛法 (1尺6寸2分 = 1.62尺)
斛法 = Fraction(162, 100)  # Represented as a fraction for precision

# 計算倉的體積
體積 = 從 * 廣 * 高  # 體積 = 長 × 寬 × 高 (單位: 尺³)

# 以斛法除之，得斛數
斛數 = Fraction(體積, 斛法)

# 分離整斛和餘分
a = int(斛數)  # 整斛數
b = (斛數 - a) * 100  # 餘分 (以百分之一斛為單位)

a, b = a, int(b)  # 答案為整數部分和餘分部分
"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 3"""

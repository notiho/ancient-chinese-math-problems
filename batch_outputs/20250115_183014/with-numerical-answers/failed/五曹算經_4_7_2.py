"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a(=228703/100)斛 奇 b(=57/50)分 。
"""

"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Take the length of 1 zhang 9 chi and multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then, multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide this by the dou divisor, which is 1 chi 6 cun 2 fen (1.62 chi), to obtain the result.

Answer: *a*(=228703/100) dou and *b*(=57/50) fen.
"""

from fractions import Fraction

# 倉從一丈九尺
從 = 1 * 10 + 9  # Convert 1 zhang 9 chi to chi (1 zhang = 10 chi)

# 廣一丈五尺
廣 = 1 * 10 + 5  # Convert 1 zhang 5 chi to chi

# 高一丈三尺
高 = 1 * 10 + 3  # Convert 1 zhang 3 chi to chi

# 列從一丈九尺以廣一十五尺乘之得二百八十五尺
底面積 = 從 * 廣  # 285 chi²

# 又以高一十三尺乘之得三千七百五尺
體積 = 底面積 * 高  # 3705 chi³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi (1.62 chi)

# 以斛法一尺六寸二分除之即得
受粟 = Fraction(體積, 斛法)  # Result in dou

# 分解結果為斛和分
a = 受粟  # 228703/100 dou
b = 受粟 - int(受粟)  # Fractional part in dou (57/50 dou)
"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 61750/27
Variable 'b' has wrong value. Expected: 57/50, Actual: 1/27"""

"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

The procedure says: Place the length of 1 zhang 9 chi and multiply it by the width of 1 zhang 5 chi, obtaining 285 chi².
Then multiply it by the height of 1 zhang 3 chi, obtaining 3705 chi³.
Divide it by the dou divisor, which is 1 chi 6 cun 2 fen, to obtain the result.

Answer: *a* dou and *b* fen.
"""

from fractions import Fraction

# 倉的尺寸
從 = 1 * 10 + 9  # 1丈9尺 = 19尺
廣 = 1 * 10 + 5  # 1丈5尺 = 15尺
高 = 1 * 10 + 3  # 1丈3尺 = 13尺

# 斛法
斛法 = 1 * 10 + 6 + Fraction(2, 10)  # 1尺6寸2分 = 16.2尺

# 列從一丈九尺以廣一十五尺乘之
底面積 = 從 * 廣  # 單位: 尺²

# 又以高一十三尺乘之
體積 = 底面積 * 高  # 單位: 尺³

# 以斛法一尺六寸二分除之
粟量 = Fraction(體積, 斛法)  # 單位: 斛

# 分離整數部分和分數部分
a = 粟量.numerator // 粟量.denominator  # 整數部分 (斛)
b = 粟量 - a  # 剩餘分數部分 (分)
b = b * 斛法  # 換算回分的單位

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 228
Variable 'b' has wrong value. Expected: 57/50, Actual: 57/5"""

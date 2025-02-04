"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 倉從一丈九尺
從 = 10 * 1 + 9  # 1丈9尺 = 10尺 + 9尺

# 廣一丈五尺
廣 = 10 * 1 + 5  # 1丈5尺 = 10尺 + 5尺

# 高一丈三尺
高 = 10 * 1 + 3  # 1丈3尺 = 10尺 + 3尺

# 列從一丈九尺以廣一十五尺乘之得二百八十五尺
底積 = 從 * 廣  # 底積 = 從 * 廣

# 又以高一十三尺乘之得三千七百五尺
體積 = 底積 * 高  # 體積 = 底積 * 高

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1尺6寸2分 = 1 + 6/10 + 2/100

# 以斛法除之即得
受粟 = Fraction(體積, 斛法)

# 答曰：a斛 奇 b分
a = 受粟.numerator // 受粟.denominator  # 取整數部分
b = Fraction(受粟.numerator % 受粟.denominator, 受粟.denominator)  # 取分數部分
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 1/27"""

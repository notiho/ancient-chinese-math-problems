"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
術曰：列從一丈九尺以廣一十五尺乘之得二百八十五尺又以高一十三尺乘之得三千七百五尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""

"""


from fractions import Fraction

# 倉從一丈九尺
從 = 10 * 1 + 9  # 1丈9尺 = 10尺 + 9尺

# 廣一丈五尺
廣 = 10 * 1 + 5  # 1丈5尺 = 10尺 + 5尺

# 高一丈三尺
高 = 10 * 1 + 3  # 1丈3尺 = 10尺 + 3尺

# 列從一丈九尺以廣一十五尺乘之得二百八十五尺
底面積 = 從 * 廣

# 又以高一十三尺乘之得三千七百五尺
體積 = 底面積 * 高

# 斛法一尺六寸二分 (1斛 = 1尺6寸2分 = 1.62尺)
斛法 = Fraction(162, 100)  # 1.62 expressed as a fraction

# 以斛法除之即得
總斛數 = Fraction(體積, 斛法)

# 分離整斛與分
a = 總斛數.numerator // 總斛數.denominator  # 整斛數
b = 總斛數 - a  # 剩餘部分 expressed as a fraction


"""

"""


"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 2287
Variable 'b' has wrong value. Expected: 57/50, Actual: 1/27"""

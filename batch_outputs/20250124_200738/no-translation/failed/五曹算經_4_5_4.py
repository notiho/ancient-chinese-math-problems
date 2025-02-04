"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 列從一丈三尺
從 = 1 * 10 + 3  # 1丈3尺 = 13尺

# 廣六尺
廣 = 6  # 6尺

# 深一丈
深 = 1 * 10  # 1丈 = 10尺

# 以廣六尺乘之得七十八尺
積1 = 從 * 廣  # 13 * 6 = 78尺²

# 以深一丈乘之得七百八十尺
積2 = 積1 * 深  # 78 * 10 = 780尺³

# 斛法：1斛 = 100尺³
斛法 = 100

# 以斛法除之即得
斛數 = Fraction(積2, 斛法)  # 780 / 100

# 答案分為斛和寸
a = int(斛數)  # 整數部分為斛數
b = (斛數 - a) * 100  # 小數部分轉為寸

# 答曰：a斛 奇 b寸
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 7
Variable 'b' has wrong value. Expected: 39/5, Actual: 80"""

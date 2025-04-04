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
積 = 從 * 廣  # 得積 78平方尺

# 以深一丈乘之得七百八十尺
體積 = 積 * 深  # 得體積 780立方尺

# 斛法：1斛 = 10立方尺
斛法 = 10

# 以斛法除之即得
斛數 = Fraction(體積, 斛法)  # 780 / 10 = 78斛

# 分離斛數與餘寸
a = int(斛數)  # 斛數的整數部分
b = (斛數 - a) * 10  # 餘寸部分

a斛 = a
b寸 = b
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""

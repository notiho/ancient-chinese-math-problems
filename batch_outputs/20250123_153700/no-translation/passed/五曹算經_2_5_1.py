"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

"""

"""


from fractions import Fraction

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸，轉化為尺
# 一丈 = 10 尺, 所以 2 丈 = 20 尺
丈 = 20
尺 = 8
寸 = Fraction(5, 10)  # 一尺 = 10 寸
絹每人 = 丈 + 尺 + 寸

# 以絹二十八尺五寸乘之
總絹尺 = 兵 * 絹每人

# 得三萬八千八百一十七尺，以四十尺除之即得
每疋尺 = 40
a = Fraction(總絹尺, 每疋尺)


"""

"""


"""
"""

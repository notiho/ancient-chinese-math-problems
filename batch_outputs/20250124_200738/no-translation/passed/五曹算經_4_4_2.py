"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 圓囷周三丈
周 = 3 * 10  # 1丈 = 10尺

# 高一丈六尺
高 = 1 * 10 + 6  # 1丈 = 10尺

# 列周三丈自相乘得九百尺
積 = 周 * 周

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 積 * 高

# 以十二除之得一千二百尺
體積 = Fraction(體積, 12)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1尺6寸2分

# 以斛法除之即得
總斛 = Fraction(體積, 斛法)

# 分離整斛與餘尺
a = int(總斛)  # 整斛部分
b = 總斛 - a  # 餘尺部分
b = b * 斛法  # 換算回尺

# 答案
a斛 = a
b尺 = b
#----- content ends here -----


"""

"""


"""
"""

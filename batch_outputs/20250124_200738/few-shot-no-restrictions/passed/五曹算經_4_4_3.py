"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang, square it to get 900 chi².
Multiply this by the height of 1 zhang 6 chi to get 14400 chi³.
Divide this by 12 to get 1200 chi³.
Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen) to get the result.

Answer: *a* hu and *b* chi³.
"""

from fractions import Fraction

# 圓囷周三丈
周 = 3  # in zhang

# 高一丈六尺
高 = 1 + Fraction(6, 10)  # 1 zhang + 6 chi (converted to zhang)

# 1丈 = 10尺, so convert 周 to chi
周_in_chi = 周 * 10  # 周 = 30 chi

# 列周三丈自相乘得九百尺
周平方 = 周_in_chi ** 2  # 周平方 = 900 chi²

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 周平方 * (高 * 10)  # 體積 = 14400 chi³

# 以十二除之得一千二百尺
體積_簡化 = 體積 // 12  # 體積_簡化 = 1200 chi³

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 斛法 = 1.62 chi³

# 以斛法除之即得
總斛數 = Fraction(體積_簡化, 斛法)

# 分解為整斛和剩餘尺³
a = int(總斛數)  # 整斛數
b = (總斛數 - a) * 斛法  # 剩餘尺³

# 答案
a, b#----- content ends here -----

"""
"""

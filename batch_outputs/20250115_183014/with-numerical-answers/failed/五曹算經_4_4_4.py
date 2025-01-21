"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a(=740)斛 奇 b(=6/5)尺 。
"""

"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang, multiply it by itself, obtaining 900 chi.
Multiply this by the height of 1 zhang 6 chi, obtaining 14400 chi.
Divide this by 12, obtaining 1200 chi.
Divide this by the hu divisor of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a*(=740) hu and *b*(=6/5) chi.
"""

from fractions import Fraction

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘得九百尺
積 = 周 * 周  # 900 chi²

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 積 * 高  # 14400 chi³

# 以十二除之得一千二百尺
體積 = Fraction(體積, 12)  # 1200 chi³

# 以斛法一尺六寸二分除之即得
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen = 1.62 chi
結果 = Fraction(體積, 斛法)

# 答：a斛 奇 b尺
a = 結果.numerator // 結果.denominator  # Integer part (740 hu)
b = Fraction(結果.numerator % 結果.denominator, 結果.denominator)  # Fractional remainder (6/5 chi)
"""
Variable 'b' has wrong value. Expected: 6/5, Actual: 20/27"""

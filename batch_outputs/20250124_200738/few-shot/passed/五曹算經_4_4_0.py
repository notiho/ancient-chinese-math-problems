"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang and multiply it by itself, obtaining 900 chi.
Multiply this by the height of 1 zhang 6 chi, obtaining 14,400 chi.
Divide this by 12, obtaining 1,200 chi.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen, and the result is the amount.

Answer: *a* hu and *b* chi.
"""

from fractions import Fraction

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘得九百尺
積 = 周 * 周

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 積 * 高

# 以十二除之得一千二百尺
體積 = Fraction(體積, 12)

# 以斛法一尺六寸二分除之即得
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi
a = int(體積 // 斛法)  # Number of hu
b = 體積 % 斛法  # Remaining chi#----- content ends here -----

"""
"""

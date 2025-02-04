"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

"""
Suppose there is a circular granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang, square it to get 900 chi².
Multiply this by the height of 1 zhang 6 chi to get 14,400 chi³.
Divide this by 12 to get 1,200 chi³.
Finally, divide this by the volume of 1 hu, which is 1 chi 6 cun 2 fen, to obtain the result.

Answer: *a* hu and *b* chi³.
"""

from fractions import Fraction

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘得九百尺
周平方 = 周 * 周

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 周平方 * 高

# 以十二除之得一千二百尺
體積除以十二 = Fraction(體積, 12)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi

# 以斛法除之即得
總斛數 = Fraction(體積除以十二, 斛法)

# 分離整斛與餘數
a = 總斛數.numerator // 總斛數.denominator  # 整斛數
b = 總斛數 - a  # 餘數部分
b = b * 斛法  # 餘數轉為 chi³

a = int(a)
b = float(b)  # 餘數以 chi³ 表示
"""
Variable 'b' has wrong value. Expected: 6/5, Actual: 1.2"""

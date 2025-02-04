"""
今有圓囷周三丈高一丈六尺問受粟㡬何
術曰列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b尺 
"""

"""
Suppose there is a circular granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang and multiply it by itself, obtaining 900 chi.
Multiply this by the height of 1 zhang 6 chi, obtaining 14,400 chi.
Divide this by 12, obtaining 1,200 chi.
Divide this by the dou-measure of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a* hu and *b* chi.
"""

from fractions import Fraction

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘得九百尺
積1 = 周 * 周

# 以高一丈六尺乘之得一萬四千四百尺
積2 = 積1 * 高

# 以十二除之得一千二百尺
積3 = Fraction(積2, 12)

# 以斛法一尺六寸二分除之
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi
結果 = Fraction(積3, 斛法)

# 分解為斛和奇尺
a = 結果.numerator // 結果.denominator  # 整數部分為斛
b = 結果 - a  # 餘數部分為奇尺

b = b * 斛法  # Convert the remainder back to chi

a = int(a)
b = float(b)  # Convert b to a decimal for clarity
"""
Variable 'b' has wrong value. Expected: 6/5, Actual: 1.2"""

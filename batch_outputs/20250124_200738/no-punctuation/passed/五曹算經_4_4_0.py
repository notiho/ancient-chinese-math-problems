"""
今有圓囷周三丈高一丈六尺問受粟㡬何
術曰列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b尺 
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 3 zhang and multiply it by itself, obtaining 900 chi².
Multiply this by the height of 1 zhang 6 chi, obtaining 14400 chi³.
Divide this by 12, obtaining 1200 chi³.
Divide this by the dou divisor of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a* hu and *b* chi.
"""

from fractions import Fraction

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘得九百尺
周平方 = 周 * 周

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 周平方 * 高

# 以十二除之得一千二百尺
體積 = Fraction(體積, 12)

# 以斛法一尺六寸二分除之即得
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi
總斛 = Fraction(體積, 斛法)

# 分離整斛和餘尺
a = int(總斛)  # 整斛數
b = (總斛 - a) * 斛法  # 餘尺數

a, b#----- content ends here -----

"""
"""

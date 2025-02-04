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

# 周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to chi

# 列周三丈自相乘得九百尺
底面積 = 周 ** 2

# 以高一丈六尺乘之得一萬四千四百尺
體積 = 底面積 * 高

# 以十二除之得一千二百尺
有效體積 = Fraction(體積, 12)

# 以斛法一尺六寸二分除之即得
總斛數 = 有效體積 / 斛法

# 分離整斛和餘數
a = int(總斛數)  # 整斛數
b = 有效體積 % 斛法  # 餘數（以尺³為單位）

a, b#----- content ends here -----

"""
"""

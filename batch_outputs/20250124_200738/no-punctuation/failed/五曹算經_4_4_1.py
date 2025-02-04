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
Divide this by the dou-measure of 1 chi 6 cun 2 fen, obtaining the result.

The answer says: *a* hu and *b* chi.
"""

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘，得九百尺
周平方 = 周 * 周

# 以高一丈六尺乘之，得一萬四千四百尺
體積 = 周平方 * 高

# 以十二除之，得一千二百尺
體積 = Fraction(體積, 12)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to chi

# 以斛法除之，即得
總斛數 = Fraction(體積, 斛法)

# 分解為整斛和餘尺
a = 總斛數.numerator // 總斛數.denominator  # 整斛數
b = Fraction(總斛數.numerator % 總斛數.denominator, 總斛數.denominator)  # 餘尺#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 6/5, Actual: 20/27"""

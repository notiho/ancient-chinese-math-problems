"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a(=15)畝 奇 b(=140)步 。
"""

#----- content starts here -----
"""
Suppose there is a drum-shaped field. The two ends are each 40 bu wide, the middle is 52 bu wide, and the length is 85 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 132 bu. Divide it by 3, obtaining 44 bu. Multiply it by the length of 85 bu, obtaining 3740 bu. Divide it by the mu-divisor, and the result is obtained.

Answer: *a*(=15) mu and *b*(=140) bu.
"""

from fractions import Fraction

# 两頭各廣四十步
廣1 = 40
廣2 = 40

# 中央廣五十二步
中央廣 = 52

# 從八十五步
從 = 85

# 并三廣得一百三十二步
三廣 = 廣1 + 廣2 + 中央廣

# 以三除之得四十四步
平均廣 = Fraction(三廣, 3)

# 以從八十五步乘之得三千七百四十步
積步 = 平均廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 整數部分為畝，餘數為步
a = 畝數.numerator // 畝數.denominator  # 15 畝
b = 畝數.numerator % 畝數.denominator  # 140 步#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 140, Actual: 7"""

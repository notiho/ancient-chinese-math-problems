"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a(=15)畝 奇 b(=140)步 。
"""

#----- content starts here -----
"""
Suppose there is a drum-shaped field where both ends are 40 bu wide, the middle is 52 bu wide, and the length is 85 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 132 bu. Divide by 3, obtaining 44 bu.
Multiply this by the length of 85 bu, obtaining 3740 bu.
Divide by the mu-divisor (240 bu), obtaining the result.

The answer says: *a*(=15) mu and *b*(=140) bu.
"""

# 两頭各廣四十步
廣_頭 = 40

# 中央廣五十二步
廣_中 = 52

# 從八十五步
從 = 85

# 并三廣得一百三十二步
三廣 = 廣_頭 + 廣_頭 + 廣_中

# 以三除之得四十四步
平均廣 = Fraction(三廣, 3)

# 以從八十五步乘之得三千七百四十步
積步 = 平均廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator  # 15

# 餘數部分為步
b = 畝數.numerator % 畝數.denominator  # 140#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 140, Actual: 7"""

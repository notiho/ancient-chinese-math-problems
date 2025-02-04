"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步問為田㡬何
術曰并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a drum-shaped field. The two ends are each 40 bu wide, and the middle is 52 bu wide. The length is 85 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 132 bu. Divide it by 3, obtaining 44 bu. Multiply it by the length of 85 bu, obtaining 3740 bu². Divide it by the mu-divisor (240), and the result is the area in mu.

Answer: *a* mu and *b* bu².
"""

# 两頭各廣四十步
廣1 = 40
廣2 = 40

# 中央廣五十二步
廣3 = 52

# 從八十五步
從 = 85

# 并三廣得一百三十二步
總廣 = 廣1 + 廣2 + 廣3

# 以三除之得四十四步
平均廣 = Fraction(總廣, 3)

# 以從八十五步乘之得三千七百四十步
積步 = 平均廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 餘步

a畝 = a
b步 = b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 140, Actual: 7"""

"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步問為田㡬何
術曰并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a waist-drum-shaped field. The length is 82 bu, the two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide by 3, obtaining 24 bu. Multiply this by the length of 82 bu, obtaining 1968 bu. Divide by the mu-divisor (240 bu), and the result is the size of the field.

Answer: *a* mu and *b* bu.
"""

# 從八十二步
從步數 = 82

# 两頭各廣三十步
兩頭廣 = 30

# 中央廣十二步
中央廣 = 12

# 并三廣得七十二步
總廣 = 兩頭廣 + 兩頭廣 + 中央廣

# 以三除之得二十四步
平均廣 = Fraction(總廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從步數

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 餘步數
"""
Variable 'b' has wrong value. Expected: 48, Actual: 1"""

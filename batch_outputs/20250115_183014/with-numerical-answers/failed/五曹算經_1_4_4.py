"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a(=8)畝 奇 b(=48)步 。
"""

"""
Suppose there is a waist-drum-shaped field (a trapezoidal field) with a length of 82 bu.
Both ends have a width of 30 bu, and the middle has a width of 12 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide this by 3, obtaining 24 bu.
Multiply this by the length of 82 bu, obtaining 1968 bu².
Divide this by the mu-divisor (240 bu²), and the result is the area.

Answer: *a*(=8) mu and *b*(=48) bu².
"""

# 從八十二步
從 = 82

# 两頭各廣三十步
廣頭 = 30

# 中央廣十二步
廣中 = 12

# 并三廣得七十二步
三廣 = 廣頭 + 廣頭 + 廣中

# 以三除之得二十四步
平均廣 = Fraction(三廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和奇步
a = 畝數.numerator // 畝數.denominator  # 整畝部分 (8)
b = 畝數.numerator % 畝數.denominator  # 奇步部分 (48)
"""
Variable 'b' has wrong value. Expected: 48, Actual: 1"""

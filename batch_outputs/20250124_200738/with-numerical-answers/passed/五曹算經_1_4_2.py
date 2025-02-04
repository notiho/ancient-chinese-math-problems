"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a(=8)畝 奇 b(=48)步 。
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field. The length is 82 bu, the width at both ends is 30 bu, and the width at the center is 12 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide by 3, obtaining 24 bu.
Multiply this by the length of 82 bu, obtaining 1968 bu.
Divide by the mu-divisor (240 bu), obtaining the result.

Answer: *a*(=8) mu and *b*(=48) bu.
"""

from fractions import Fraction

# 從八十二步
從 = 82

# 两頭各廣三十步
兩頭廣 = 30

# 中央廣十二步
中央廣 = 12

# 并三廣得七十二步
三廣 = 兩頭廣 + 兩頭廣 + 中央廣

# 以三除之得二十四步
平均廣 = Fraction(三廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 答曰： a(=8)畝 奇 b(=48)步
a = 畝數.numerator // 畝數.denominator  # 8 畝
b = 積步 % 畝法  # 48 步#----- content ends here -----

"""
"""

"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步問為田㡬何
術曰并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field. The length is 82 bu.
The two ends each have a width of 30 bu, and the center has a width of 12 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu.
Divide by 3, obtaining 24 bu.
Multiply this by the length of 82 bu, obtaining 1968 bu².
Divide by the mu-divisor (240 bu²), obtaining the result.

Answer: *a* mu and *b* bu².
"""

from fractions import Fraction

# 從八十二步
從步數 = 82

# 两頭各廣三十步
頭廣 = 30

# 中央廣十二步
中央廣 = 12

# 并三廣得七十二步
總廣 = 頭廣 + 頭廣 + 中央廣

# 以三除之得二十四步
平均廣 = Fraction(總廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從步數

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分離畝和步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 48, Actual: 1"""

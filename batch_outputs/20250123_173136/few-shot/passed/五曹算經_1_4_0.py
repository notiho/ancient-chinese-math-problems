"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a waist-drum-shaped field with a length of 82 bu.
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu.
Divide it by 3, obtaining 24 bu.
Multiply it by the length of 82 bu, obtaining 1968 bu.
Divide it by the mu-divisor (240 bu), obtaining the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 從八十二步
從 = 82

# 兩頭各廣三十步
廣1 = 30
廣2 = 30

# 中央廣十二步
廣3 = 12

# 并三廣得七十二步
總廣 = 廣1 + 廣2 + 廣3

# 以三除之得二十四步
平均廣 = 總廣 // 3

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 積步 % 畝法  # 餘步
"""
"""

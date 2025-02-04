"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field (trapezoidal field) with a length of 82 bu.
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

The procedure says: Add the three widths together, obtaining 72 bu.
Divide this by 3, obtaining 24 bu.
Multiply this by the length (82 bu), obtaining 1968 bu.
Divide this by the mu-divisor (240 bu), obtaining the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 田從八十二步
從 = 82

# 兩頭各廣三十步
廣_頭 = 30

# 中央廣十二步
廣_中 = 12

# 并三廣得七十二步
總廣 = 廣_頭 + 廣_頭 + 廣_中

# 以三除之得二十四步
平均廣 = Fraction(總廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從

# 以畝法二百四十步除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分解為整畝和奇步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 奇步

a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 48, Actual: 1"""

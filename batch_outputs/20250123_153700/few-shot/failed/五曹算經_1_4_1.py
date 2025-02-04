"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a waist-drum-shaped field. The length is 82 bu. 
The widths at both ends are 30 bu each, and the width at the center is 12 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide it by 3, obtaining 24 bu. 
Multiply it by the length, 82 bu, obtaining 1968 bu². 
Divide it by the mu-divisor (240 bu² per mu), and the result is the area.

The answer says: *a* mu and *b* bu.
"""

from fractions import Fraction

# 從八十二步
從 = 82

# 兩頭各廣三十步
廣頭 = 30

# 中央廣十二步
廣中 = 12

# 并三廣得七十二步
總廣 = 廣頭 + 廣頭 + 廣中

# 以三除之得二十四步
平均廣 = Fraction(總廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離整畝與餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 餘步數

a, b  # Output the result as a mu and b bu
"""
Variable 'b' has wrong value. Expected: 48, Actual: 1"""

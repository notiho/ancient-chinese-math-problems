"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a drum-shaped field with two ends each having a width of 40 bu, the middle having a width of 52 bu, and a length of 85 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 132 bu. Divide it by 3, obtaining 44 bu. Multiply it by the length, 85 bu, obtaining 3740 bu. Divide it by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
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
總廣 = 廣1 + 廣2 + 中央廣

# 以三除之
平均廣 = Fraction(總廣, 3)

# 以從八十五步乘之
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator

# 餘數部分為步
b = 畝數.numerator % 畝數.denominator

a, b
"""
Variable 'b' has wrong value. Expected: 140, Actual: 7"""

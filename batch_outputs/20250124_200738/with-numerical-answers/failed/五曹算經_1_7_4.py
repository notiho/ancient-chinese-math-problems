"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
術曰：并三廣得一百八步以三除之得三十六步以從九十二步乘之得三千三百一十二步以畝法除之即得。
答曰： a(=13)畝 奇 b(=192)步 。
"""

#----- content starts here -----
"""
Suppose there is a snake-shaped field. The width at the head is 33 bu, the width at the middle is 57 bu, the width at the tail is 18 bu, and the length is 92 bu.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 108 bu. Divide it by 3, obtaining 36 bu. Multiply it by the length, 92 bu, obtaining 3312 bu. Divide it by the mu-divisor, 240, to obtain the result.

Answer: *a*(=13) mu and *b*(=192) bu.
"""

# 頭廣三十三步
頭廣 = 33

# 胷廣五十七步
胷廣 = 57

# 尾廣十八步
尾廣 = 18

# 從九十二步
從 = 92

# 并三廣得一百八步
總廣 = 頭廣 + 胷廣 + 尾廣

# 以三除之得三十六步
平均廣 = Fraction(總廣, 3)

# 以從九十二步乘之得三千三百一十二步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator  # 13

# 餘數部分為步
b = 畝數.numerator % 畝數.denominator  # 192#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 192, Actual: 4"""

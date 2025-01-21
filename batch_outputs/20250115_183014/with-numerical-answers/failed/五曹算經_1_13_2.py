"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a(=3)畝 奇 b(=80)步 。
"""

"""
Suppose there is an irregular quadrilateral field with the following dimensions:
East side: 35 bu, West side: 45 bu, South side: 25 bu, North side: 15 bu.
Question: how large is the area of the field?

The procedure says: Add the east and west sides, obtaining 80 bu, and take half of it, obtaining 40 bu.
Then add the south and north sides, obtaining 40 bu, and take half of it, obtaining 20 bu.
Multiply these two results, obtaining 800 bu².
Divide by the mu-divisor (240 bu²), and the result is the area in mu.

Answer: *a*(=3) mu and remainder *b*(=80) bu².
"""

# 東三十五步
東 = 35

# 西四十五步
西 = 45

# 南二十五步
南 = 25

# 北一十五步
北 = 15

# 并東西得八十步半之得四十步
東西和 = 東 + 西
東西半 = 東西和 / 2

# 并南北得四十步半之得二十步
南北和 = 南 + 北
南北半 = 南北和 / 2

# 二位相乘得八百步
積步 = 東西半 * 南北半

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 整數部分為畝，餘數部分為步
a = 畝數.numerator // 畝數.denominator  # 3 畝
b = 畝數.numerator % 畝數.denominator  # 80 步
"""
Code error: both arguments should be Rational instances"""

"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a(=3)畝 奇 b(=80)步 。
"""

#----- content starts here -----
"""
Suppose there is an irregular quadrilateral field with the following dimensions:
East side: 35 bu, West side: 45 bu, South side: 25 bu, North side: 15 bu.
Question: how large is the field?

The procedure says: Add the east and west sides, obtaining 80 bu, and halve it, obtaining 40 bu.
Then add the south and north sides, obtaining 40 bu, and halve it, obtaining 20 bu.
Multiply the two results, obtaining 800 bu.
Divide by the mu-divisor (240), and the result is obtained.

Answer: *a*(=3) mu and remainder *b*(=80) bu.
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
東西平均 = (東 + 西) / 2

# 并南北得四十步半之得二十步
南北平均 = (南 + 北) / 2

# 二位相乘得八百步
積步 = 東西平均 * 南北平均

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator  # 3

# 餘數部分為步
b = 畝數.numerator % 畝數.denominator  # 80#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

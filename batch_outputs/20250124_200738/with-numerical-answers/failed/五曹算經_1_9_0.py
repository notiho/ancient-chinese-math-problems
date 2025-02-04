"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a(=6)畝
"""

#----- content starts here -----
"""
Suppose there is a field shaped like a trapezoid, with one side of length 48 bu, one width of 25 bu, and the other width of 35 bu.
Question: how large is the field?

The procedure says: Add the two widths, obtaining 60 bu. Halve it, obtaining 30 bu. Multiply it by the length of 48 bu, obtaining 1440 bu². Divide it by the mu-divisor (240), and the result is the number of mu.

Answer: *a*(=6) mu.
"""

# 從四十八步
從步數 = 48

# 一頭廣二十五步
廣一 = 25

# 一頭廣三十五步
廣二 = 35

# 并二廣得六十步
廣和 = 廣一 + 廣二

# 半之得三十步
平均廣 = 廣和 / 2

# 以從四十八步乘之得一千四百四十步
積步 = 平均廣 * 從步數

# 以畝法除之即得
畝法 = 240
a = Fraction(積步, 畝法) # 6#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

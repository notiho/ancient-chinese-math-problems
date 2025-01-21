"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a畝
"""

"""
Suppose there is a field shaped like a trapezoid, with one side of length 48 bu, one base width of 25 bu, and the other base width of 35 bu.
Question: how large is the field?

The procedure says: Add the two widths, obtaining 60 bu. Halve this, obtaining 30 bu. Multiply it by the length of 48 bu, obtaining 1440 bu. Divide this by the mu-divisor (240), and the result is the number of mu.

Answer: *a* mu.
"""

# 從四十八步
從步數 = 48

# 一頭廣二十五步
廣一 = 25

# 一頭廣三十五步
廣二 = 35

# 并二廣得六十步
總廣 = 廣一 + 廣二

# 半之得三十步
平均廣 = Fraction(總廣, 2)

# 以從四十八步乘之得一千四百四十步
積步 = 平均廣 * 從步數

# 以畝法除之即得
畝法 = 240
a = Fraction(積步, 畝法)
"""
"""

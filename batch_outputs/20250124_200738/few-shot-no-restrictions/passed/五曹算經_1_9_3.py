"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
術曰：并二廣得六十步半之得三十步以從四十八步乘之得一千四百四十步以畝法除之即得。
答曰： a畝
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field where one side of the width is 25 bu, the other side of the width is 35 bu, and the length is 48 bu.
Question: how large is the field?

The procedure says: Add the two widths, obtaining 60 bu. Halve it, obtaining 30 bu.
Multiply this by the length of 48 bu, obtaining 1440 bu².
Divide it by the mu-divisor (240 bu² per mu), and the result is the area in mu.

Answer: *a* mu.
"""

from fractions import Fraction

# 一頭廣 25 步
廣1 = 25

# 一頭廣 35 步
廣2 = 35

# 從 48 步
從 = 48

# 并二廣得六十步
總廣 = 廣1 + 廣2

# 半之得三十步
平均廣 = Fraction(總廣, 2)

# 以從四十八步乘之得一千四百四十步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
a = Fraction(積步, 畝法)

# Output the result
a#----- content ends here -----

"""
"""

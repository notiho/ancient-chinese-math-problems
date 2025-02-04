"""
今有箕田一頭廣八十六步一頭廣四十步從九十步問為田㡬何
術曰并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field, with one side of width 86 bu, the other side of width 40 bu, and a length of 90 bu.
Question: how large is the field?

The procedure says: Add the two widths, obtaining 126 bu. Halve it, obtaining 63 bu.
Multiply it by the length of 90 bu, obtaining 5670 bu².
Divide it by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 一頭廣八十六步
廣1 = 86

# 一頭廣四十步
廣2 = 40

# 從九十步
從 = 90

# 并二廣得一百二十六步
并廣 = 廣1 + 廣2

# 半之得六十三步
平均廣 = Fraction(并廣, 2)

# 以從九十步乘之，得五千六百七十步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator

# 餘數部分為奇步
b = 畝數.numerator % 畝數.denominator

a畝 = a
b步 = b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 150, Actual: 5"""

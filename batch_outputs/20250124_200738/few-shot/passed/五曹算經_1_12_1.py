"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field, with one side of width 86 bu, the other side of width 40 bu, and a length of 90 bu.
Question: how large is the field?

The procedure says: Add the two widths, obtaining 126 bu. Halve it, obtaining 63 bu.
Multiply it by the length, obtaining 5670 bu.
Divide it by the mu-divisor (240), and the result is obtained.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

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

# 以從九十步乘之得五千六百七十步
積步 = 平均廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = 積步 // 畝法  # 整數部分為畝
餘步 = 積步 % 畝法  # 餘數為步

a = 畝數
b = 餘步#----- content ends here -----

"""
"""

"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field, one side is 86 bu wide, the other side is 40 bu wide, and the length is 90 bu.
Question: how large is the field?

The procedure says: Add the two widths, obtaining 126 bu. Halve it, obtaining 63 bu.
Multiply it by the length (90 bu), obtaining 5670 bu².
Divide it by the mu-divisor (240 bu² per mu), obtaining the result.

Answer: *a* mu and *b* bu².
"""

from fractions import Fraction

# 一頭廣八十六步
廣1 = 86

# 一頭廣四十步
廣2 = 40

# 從九十步
從 = 90

# 并二廣得一百二十六步
總廣 = 廣1 + 廣2

# 半之得六十三步
平均廣 = Fraction(總廣, 2)

# 以從九十步乘之得五千六百七十步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和剩餘步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

print(f"答曰：{a} 畝 奇 {b} 步。")#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 150, Actual: 5"""

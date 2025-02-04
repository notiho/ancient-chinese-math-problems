"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field. One side of the length is 30 bu, one side of the width is 24 bu, and the other side of the width is 0 bu.
Question: how large is the field?

The procedure says: Take one side of the width (24 bu), halve it to get 12 bu. Multiply this by the length (30 bu) to get the total area in bu². Divide the result by the mu-divisor (240 bu² per mu) to get the area in mu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given dimensions
從 = 30  # Length in bu
廣一頭 = 24  # Width of one side in bu
廣另一頭 = 0  # Width of the other side in bu

# Halve the width (average width of the wedge)
平均廣 = Fraction(廣一頭 + 廣另一頭, 2)

# Calculate the total area in bu²
積步 = 平均廣 * 從

# 畝法: 240 bu² per mu
畝法 = 240

# Convert the area into mu and remaining bu
畝數 = 積步 // 畝法  # Integer part (whole mu)
剩餘步 = 積步 % 畝法  # Remainder (remaining bu)

# Final answer
a = 畝數
b = 剩餘步

print(f"Answer: {a} 畝 and {b} 步.")#----- content ends here -----

"""
"""

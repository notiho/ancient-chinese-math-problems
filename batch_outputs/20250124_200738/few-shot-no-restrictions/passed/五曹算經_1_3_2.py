"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field. One end of the field has a width of 30 bu, while the other end has no width (0 bu). 
The length of the field is 24 bu.
Question: how large is the area of the field?

The procedure says: Take the width of one end (24 bu) and halve it, obtaining 12 bu. 
Multiply this by the length (30 bu), obtaining 360 bu².
Divide this by the mu-divisor (240 bu² per mu), and the result is the area in mu.

The answer says: *a* mu and *b* bu².
"""

from fractions import Fraction

# Given values
從 = 30  # Length of the field in bu
廣一頭 = 24  # Width of one end in bu
廣另一頭 = 0  # Width of the other end in bu
畝法 = 240  # Conversion factor: 240 bu² = 1 mu

# Procedure
# Halve the width of one end
平均廣 = Fraction(廣一頭, 2)

# Multiply by the length to get the total area in bu²
積步 = 平均廣 * 從

# Convert to mu
畝數 = 積步 // 畝法  # Integer part (whole mu)
餘步 = 積步 % 畝法  # Remainder (remaining bu²)

# Results
a = 畝數  # Whole mu
b = 餘步  # Remaining bu²

# Output
a, b#----- content ends here -----

"""
"""

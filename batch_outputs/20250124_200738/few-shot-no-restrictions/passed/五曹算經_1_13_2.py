"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is an irregularly shaped field with the following dimensions:
East: 35 bu, West: 45 bu, South: 25 bu, North: 15 bu.
Question: how large is the area of the field?

The procedure says: Add the east and west sides, obtaining 80 bu. Halve it, obtaining 40 bu.
Then add the south and north sides, obtaining 40 bu. Halve it, obtaining 20 bu.
Multiply the two results, obtaining 800 bu².
Divide by the mu-divisor (240 bu² per mu), obtaining the area in mu and remaining bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Dimensions of the field
東 = 35
西 = 45
南 = 25
北 = 15

# 畝法 (240 bu² per mu)
畝法 = 240

# Add east and west, then halve
東西和 = 東 + 西
東西半 = 東西和 / 2

# Add south and north, then halve
南北和 = 南 + 北
南北半 = 南北和 / 2

# Multiply the two results to get the area in bu²
積步 = 東西半 * 南北半

# Divide by 畝法 to get the area in mu and remaining bu
畝數 = 積步 // 畝法  # Integer part (whole mu)
剩餘步 = 積步 % 畝法  # Remainder (remaining bu)

# Final result
a = 畝數
b = 剩餘步

# Output the results
a, b#----- content ends here -----

"""
"""

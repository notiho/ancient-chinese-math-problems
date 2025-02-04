"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field (a trapezoidal field) with a length of 82 bu.
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

The procedure says: Add the three widths, obtaining 72 bu. Divide by 3, obtaining 24 bu.
Multiply this by the length of 82 bu, obtaining 1968 bu.
Divide by the mu-divisor (240 bu per mu), obtaining the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given values
從 = 82  # Length of the field in bu
廣1 = 30  # Width at one end in bu
廣2 = 30  # Width at the other end in bu
中央廣 = 12  # Width in the middle in bu

# Step 1: Add the three widths
總廣 = 廣1 + 廣2 + 中央廣  # Total width

# Step 2: Divide by 3 to get the average width
平均廣 = Fraction(總廣, 3)

# Step 3: Multiply the average width by the length
積步 = 平均廣 * 從  # Total area in bu²

# Step 4: Divide by 畝法 (240 bu per mu) to get the area in mu
畝法 = 240
畝數 = 積步 // 畝法  # Whole mu
餘步 = 積步 % 畝法  # Remaining bu

# Final answer
a = 畝數
b = 餘步

a, b#----- content ends here -----

"""
"""

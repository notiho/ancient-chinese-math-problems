"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field (trapezoidal field) with a length of 82 bu.
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

The procedure says: Add the three widths together, obtaining 72 bu.
Divide by 3, obtaining 24 bu.
Multiply this by the length of 82 bu, obtaining 1968 bu².
Divide this by the mu-divisor (240 bu² per mu), and the result is the area in mu and remaining bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given data
從 = 82  # Length of the field in bu
廣_兩頭 = 30  # Width at both ends in bu
廣_中央 = 12  # Width at the center in bu
畝法 = 240  # Conversion factor: 240 bu² = 1 mu

# Step 1: Add the three widths together
總廣 = 廣_兩頭 + 廣_兩頭 + 廣_中央  # Total width

# Step 2: Divide by 3 to get the average width
平均廣 = Fraction(總廣, 3)

# Step 3: Multiply the average width by the length
積步 = 平均廣 * 從  # Total area in bu²

# Step 4: Divide by the mu-divisor to get the area in mu and remaining bu
畝數 = 積步 // 畝法  # Whole mu
餘步 = 積步 % 畝法  # Remaining bu

# Final answer
a = 畝數
b = 餘步

# Output
a, b#----- content ends here -----

"""
"""

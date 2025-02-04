"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is an irregular quadrilateral field with the following dimensions:
- East side: 35 bu
- West side: 45 bu
- South side: 25 bu
- North side: 15 bu

Question: How large is the area of the field?

Answer: *a* mu and *b* bu.
"""

# Dimensions of the field
東 = 35  # East side
西 = 45  # West side
南 = 25  # South side
北 = 15  # North side

# Calculate the average length (東 + 西) / 2
平均長 = Fraction(東 + 西, 2)

# Calculate the average width (南 + 北) / 2
平均寬 = Fraction(南 + 北, 2)

# Area in bu^2
田積 = 平均長 * 平均寬

# Convert to mu and bu
a = 田積 // 240  # 1 mu = 240 bu^2
b = 田積 % 240  # Remaining bu^2 after converting to mu

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
"""

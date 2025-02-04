"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is an irregular quadrilateral field with:
- East side: 35 bu
- West side: 45 bu
- South side: 25 bu
- North side: 15 bu.

Question: What is the area of the field?

Answer: *a* mu and *b* bu.
"""

# Define the sides of the field
東 = 35
西 = 45
南 = 25
北 = 15

# Calculate the average of the east and west sides
平均東西 = Fraction(東 + 西, 2)

# Calculate the average of the south and north sides
平均南北 = Fraction(南 + 北, 2)

# Calculate the area in bu^2
面積步 = 平均東西 * 平均南北

# Convert the area into mu and remaining bu
a = 面積步 // 240  # 1 mu = 240 bu^2
b = 面積步 % 240  # Remaining bu^2 after converting to mu

a, b  # Output the result as (a mu, b bu)
"""
"""

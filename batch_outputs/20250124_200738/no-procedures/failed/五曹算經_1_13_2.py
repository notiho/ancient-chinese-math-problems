"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is an irregular quadrilateral field with:
- East side = 35 bu,
- West side = 45 bu,
- South side = 25 bu,
- North side = 15 bu.

Question: How large is the area of the field?

Answer: *a* mu and *b* bu.
"""

# Define the sides of the field
東 = 35  # East side
西 = 45  # West side
南 = 25  # South side
北 = 15  # North side

# The formula for the area of an irregular quadrilateral field is:
# Area = (1/2) * (sum of opposite sides) * (sum of other opposite sides)
田積 = Fraction(1, 2) * (東 + 西) * (南 + 北)

# Convert the area into mu and remaining bu
# 1 mu = 240 bu
a = 田積 // 240  # Whole mu
b = 田積 % 240   # Remaining bu

a, b  # Output the result as a mu and b bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3, Actual: 6
Variable 'b' has wrong value. Expected: 80, Actual: 160"""

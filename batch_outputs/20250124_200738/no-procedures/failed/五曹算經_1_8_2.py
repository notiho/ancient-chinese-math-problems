"""
今有牆田方周一千步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a perimeter of 1000 bu.
Question: how large is the area of the field?

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 方周一千步 (perimeter of the square field is 1000 bu)
perimeter = 1000

# Calculate the side length of the square field
side_length = Fraction(perimeter, 4)

# Calculate the area of the field in square bu
area_in_bu = side_length * side_length

# Convert the area into qing and remaining bu
# 1 qing = 24000 square bu
a = area_in_bu // 24000  # Number of qing
b = area_in_bu % 24000   # Remaining bu

a, b  # Output the result as qing and bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 14500"""

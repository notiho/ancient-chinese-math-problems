"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree in the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

Answer: *a* qing and *b* bu.
"""

# From the problem, the diagonal of the square field is 147 bu.
diagonal = 147

# The relationship between the diagonal and the side of a square is:
# diagonal = side * sqrt(2)
# Therefore, side = diagonal / sqrt(2)

# To avoid using square roots directly, we know that the area of the square field is:
# area = (diagonal^2) / 2
area_in_bu = Fraction(diagonal**2, 2)

# Convert the area into qing and bu:
# 1 qing = 24000 bu
a = area_in_bu // 24000  # Number of qing
b = area_in_bu % 24000  # Remaining bu

# Final result:
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 0
Variable 'b' has wrong value. Expected: 180, Actual: 21609/2"""

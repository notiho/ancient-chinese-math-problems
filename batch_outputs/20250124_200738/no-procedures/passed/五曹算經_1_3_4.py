"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field (圭田) with one side of the length being 30 bu, the other side being 0 bu, and the width being 24 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

# Define the dimensions of the field
從一頭 = 30  # Length of one side in bu
從另一頭 = 0  # Length of the other side in bu
廣 = 24  # Width in bu

# Calculate the area of the wedge-shaped field
# Area = (average length) * width
area_in_bu = Fraction((從一頭 + 從另一頭), 2) * 廣

# Convert the area into mu and bu
a = area_in_bu // 240  # 1 mu = 240 bu
b = area_in_bu % 240  # Remaining bu after converting to mu

# The result is a mu and b bu
a, b#----- content ends here -----

"""
"""

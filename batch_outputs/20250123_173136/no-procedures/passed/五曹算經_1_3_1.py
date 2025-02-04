"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a wedge-shaped field (圭田) with one side of the length being 30 bu, the other side of the length being 0 bu, and the width being 24 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Dimensions of the wedge-shaped field
長一頭 = 30  # one side of the length
長另一頭 = 0  # the other side of the length
廣 = 24  # width

# The area of a wedge-shaped field is calculated as:
# Area = ( (長一頭 + 長另一頭) / 2 ) * 廣
田積 = Fraction((長一頭 + 長另一頭), 2) * 廣

# Convert the area into mu and remaining bu
# 1 畝 = 240 平方步
a = 田積 // 240  # whole mu
b = 田積 % 240  # remaining bu

a, b  # Output the result as a mu and b bu
"""
"""

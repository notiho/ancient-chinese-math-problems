"""
今有牆田方周一千步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a square field with a perimeter of 1000 bu.
Question: how large is the area of the field?

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 方周一千步 (perimeter of the square field)
周 = 1000

# Calculate the side length of the square field
邊長 = 周 / 4

# Calculate the area of the field in square bu
面積 = 邊長 * 邊長

# Convert the area into qing and bu
# 1 qing = 24000 square bu
a = 面積 // 24000  # Number of qing
b = 面積 % 24000   # Remaining bu

a = int(a)
b = int(b)

a, b
"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 14500"""

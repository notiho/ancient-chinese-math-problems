"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
答曰： a步 。
"""

"""
Suppose there is a volume of 234,567 cubic bu (步³).
Question: what is the side length of the cube (in bu)?

Answer: the side length is *a* bu.
"""

# Given volume in cubic bu
volume = 234567

# To find the side length of a cube, we take the cube root of the volume.
# Since we are working with exact arithmetic, we will find the largest integer `a` such that `a^3 <= volume`.

a = 0
while a**3 <= volume:
    a += 1

# The correct side length is one less than the last increment
a -= 1

# The side length of the cube is `a` bu.
a
"""
Variable 'a' has wrong value. Expected: 468823/968, Actual: 61"""

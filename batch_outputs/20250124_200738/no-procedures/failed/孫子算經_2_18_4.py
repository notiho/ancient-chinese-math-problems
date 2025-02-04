"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 234,567 cubic bu (步³).
Question: what is the side length of the cube if the volume is a perfect cube?

Answer: the side length is *a* bu (步).
"""

# Given volume in cubic bu
volume = 234567

# To find the side length of the cube, we need the cube root of the volume.
# Since we cannot use external libraries, we will compute it manually.

# Initialize variables
a = 0

# Incrementally find the largest integer `a` such that a³ <= volume
while a**3 <= volume:
    a += 1

# The correct side length is one less than the last increment
a -= 1

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 468823/968, Actual: 61"""

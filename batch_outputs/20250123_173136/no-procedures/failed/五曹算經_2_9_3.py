"""
今有車二萬三千九百乘，欲作方營，每乘占地三步。問：計㡬何？
答曰： a步 。
"""

"""
Suppose there are 23,900 chariots, and each chariot occupies 3 bu of land. It is desired to form a square camp.
Question: what is the side length of the square camp?

Answer: *a* bu.
"""

# 車二萬三千九百乘
車數 = 23900

# 每乘占地三步
每乘占地 = 3

# 總占地面積
總占地面積 = 車數 * 每乘占地

# 方營邊長 (side length of the square camp)
# The area of a square is side^2, so side = sqrt(area).
# To find the side length, we take the square root of the total area.
# a = sqrt(總占地面積)

# Since we cannot use external functions, we calculate the square root manually:
# Find the largest integer whose square is less than or equal to 總占地面積.
a = 1
while a * a <= 總占地面積:
    a += 1
a -= 1  # Step back to the correct value

a  # This is the side length of the square camp in bu.
"""
Variable 'a' has wrong value. Expected: 71700, Actual: 267"""

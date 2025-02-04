"""
今有車二萬三千九百乘，欲作方營，每乘占地三步。問：計㡬何？
答曰： a步 。
"""

"""
Suppose there are 23,900 chariots, and each chariot occupies 3 square bu of land. 
It is desired to arrange them into a square-shaped camp. 
Question: what is the side length of the square camp?

Answer: *a* bu.
"""

# 車二萬三千九百乘
車 = 23900

# 每乘占地三步
每車占地 = 3

# 總占地面積
總占地 = 車 * 每車占地

# 方營的邊長 (side length of the square camp)
# The side length is the square root of the total area
# Since we cannot use external functions, we approximate the square root manually.

# Start with the total area
area = 總占地

# Approximate the square root manually
a = 0
while a * a <= area:
    a += 1
a -= 1  # Step back to the largest integer whose square is less than or equal to the area

# The side length of the square camp is `a` bu.
a
"""
Variable 'a' has wrong value. Expected: 71700, Actual: 267"""

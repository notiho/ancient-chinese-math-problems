"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
答曰： a步 。
"""

"""
Suppose there is a rope that is 5794 bu long. It is desired to form it into a square.
Question: what is the side length of the square?

Answer: *a* bu.
"""

# 索長
索長 = 5794

# To form a square, the perimeter of the square is equal to the rope length.
# The perimeter of a square is 4 times the side length.
# Solve for the side length:
a = Fraction(索長, 4)  # Divide the rope length by 4 to get the side length of the square.

a
"""
"""

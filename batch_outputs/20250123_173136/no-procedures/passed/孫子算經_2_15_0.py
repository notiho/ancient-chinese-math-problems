"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
答曰： a步 。
"""

"""
Suppose there is a rope 5794 bu long. It is desired to form it into a square.
Question: what is the side length of the square?

Answer: the side length is *a* bu.
"""

# 索長
索長 = 5794

# To form a square, the total length of the rope is divided by 4 (since a square has 4 equal sides)
a = Fraction(索長, 4)  # Each side of the square in bu
"""
"""

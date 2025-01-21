"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
答曰： a步 b尺 。
"""

"""
Suppose there is a rope that is 5794 bu long. It is desired to form it into a square.
Question: what is the side length of the square?

Answer: the side length is *a* bu and *b* chi.
"""

# 索長
索長 = 5794  # in bu

# The perimeter of the square is equal to the length of the rope
# Perimeter = 4 * side_length
# side_length = 索長 / 4
side_length = Fraction(索長, 4)

# Extract the integer part (a) and the fractional part (b in chi)
a = side_length.numerator // side_length.denominator  # Integer part in bu
b = (side_length.numerator % side_length.denominator) * 10 // side_length.denominator  # Fractional part in chi (1 bu = 10 chi)

a, b  # The side length in bu and chi
"""
Variable 'b' has wrong value. Expected: 3, Actual: 5"""

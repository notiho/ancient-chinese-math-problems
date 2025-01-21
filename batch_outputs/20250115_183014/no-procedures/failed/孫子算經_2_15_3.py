"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
答曰： a步 b尺 。
"""

"""
Suppose there is a rope that is 5794 bu long. It is desired to form it into a square.
Question: what is the length of each side?

Answer: each side is *a* bu and *b* chi.
"""

# 索長 5794 步
索長 = 5794

# A square has 4 equal sides, so divide the total length by 4 to get the side length
side_length = Fraction(索長, 4)

# Extract the integer part (a) as bu
a = side_length.numerator // side_length.denominator

# Extract the fractional part and convert it to chi (1 bu = 10 chi)
b = (side_length - a) * 10

# Convert b to an integer
b = b.numerator // b.denominator

# Final result: a bu and b chi
a, b
"""
Variable 'b' has wrong value. Expected: 3, Actual: 5"""

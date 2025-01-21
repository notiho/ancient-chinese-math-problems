"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
答曰： a步 b尺 。
"""

"""
Suppose there is a rope 5794 bu long. It is desired to form it into a square.
Question: what is the length of one side of the square?

Answer: *a* bu and *b* chi.
"""

# 索長 5794 步
索長 = 5794

# The perimeter of the square is equal to the rope length
# Divide the rope length by 4 to get the side length in bu
side_length_in_bu = Fraction(索長, 4)

# Extract the integer part (a) and the fractional part (b in chi)
a = side_length_in_bu.numerator // side_length_in_bu.denominator  # Integer part in bu
b = (side_length_in_bu - a) * 10  # Convert the fractional part to chi (1 bu = 10 chi)

# Ensure b is an integer
b = b.numerator // b.denominator

a, b  # Output the result as (a bu, b chi)
"""
Variable 'b' has wrong value. Expected: 3, Actual: 5"""

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
索長 = 5794

# The perimeter of the square is equal to the length of the rope
# Divide the perimeter by 4 to get the side length in bu
side_length_in_bu = 索長 // 4

# Calculate the remainder to get the remaining length in chi (1 bu = 10 chi)
remaining_length_in_chi = (索長 % 4) * 10 // 4

# Assign the results
a = side_length_in_bu
b = remaining_length_in_chi
"""
Variable 'b' has wrong value. Expected: 3, Actual: 5"""

"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
答曰： a步 b尺 。
"""

"""
Suppose there is a rope, 5794 bu in length. It is desired to form it into a square.
Question: what is the side length of the square?

Answer: *a* bu and *b* chi.
"""

# 索長
索長 = 5794  # in bu

# To form a square, the total length of the rope is divided by 4 to get the perimeter of one side
side_length_bu = 索長 // 4  # Integer division to get the bu part
remaining_bu = 索長 % 4  # Remaining part in bu

# Convert remaining bu into chi (1 bu = 10 chi)
side_length_chi = remaining_bu * 10

# Final result
a = side_length_bu  # Side length in bu
b = side_length_chi  # Remaining length in chi
"""
Variable 'b' has wrong value. Expected: 3, Actual: 20"""

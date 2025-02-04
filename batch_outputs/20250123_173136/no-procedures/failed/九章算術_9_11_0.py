"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
Suppose there is a door of unknown height and width, and a pole of unknown length. 
When the pole is placed horizontally, it cannot extend beyond 4 chi (width). 
When it is placed vertically, it cannot extend beyond 2 chi (height). 
When it is placed diagonally, it just fits perfectly.

Question: What are the height, width, and diagonal length of the door?

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

# Given dimensions
horizontal = 4  # width in chi
vertical = 2    # height in chi

# Calculate the diagonal using the Pythagorean theorem
# Diagonal = sqrt(horizontal^2 + vertical^2)
diagonal = (horizontal**2 + vertical**2)**0.5

# Convert diagonal from chi to zhang (1 zhang = 10 chi)
diagonal_in_zhang = diagonal / 10

# Assign results
a = horizontal  # width in chi
b = vertical    # height in chi
c = diagonal_in_zhang  # diagonal in zhang

# Results
a, b, c
"""
Variable 'a' has wrong value. Expected: 6, Actual: 4
Variable 'b' has wrong value. Expected: 8, Actual: 2
Variable 'c' has wrong value. Expected: 1, Actual: 0.447213595499958"""

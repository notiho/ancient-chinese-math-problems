"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
Suppose there is a door, but its height and width are unknown. There is also a pole, but its length is unknown.
When the pole is placed horizontally, it cannot extend beyond 4 chi. When placed vertically, it cannot extend beyond 2 chi. When placed diagonally, it fits perfectly.
Question: What are the width, height, and diagonal length of the door?

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

# Given dimensions
horizontal = 4  # chi
vertical = 2    # chi

# Calculate the diagonal length using the Pythagorean theorem
diagonal = (horizontal**2 + vertical**2)**0.5  # chi

# Convert diagonal length to zhang (1 zhang = 10 chi)
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

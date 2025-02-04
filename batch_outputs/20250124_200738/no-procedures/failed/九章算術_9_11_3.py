"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

#----- content starts here -----
"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When the pole is placed horizontally, it does not extend beyond 4 chi. When placed vertically, it does not extend beyond 2 chi. When placed diagonally, it fits exactly.

Question: What are the width, height, and length of the pole?

Answer: The width is *a* chi, the height is *b* chi, and the length of the pole is *c* zhang.
"""

# Given values
horizontal = 4  # Horizontal distance (width) in chi
vertical = 2    # Vertical distance (height) in chi

# Using the Pythagorean theorem to calculate the diagonal (length of the pole)
# diagonal^2 = horizontal^2 + vertical^2
diagonal_squared = horizontal**2 + vertical**2

# Calculate the diagonal (length of the pole)
diagonal = diagonal_squared**0.5  # Square root of the sum

# Convert diagonal from chi to zhang (1 zhang = 10 chi)
diagonal_in_zhang = diagonal / 10

# Assign results
a = horizontal  # Width in chi
b = vertical    # Height in chi
c = diagonal_in_zhang  # Length of the pole in zhang

# Results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6, Actual: 4
Variable 'b' has wrong value. Expected: 8, Actual: 2
Variable 'c' has wrong value. Expected: 1, Actual: 0.447213595499958"""

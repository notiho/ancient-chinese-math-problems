"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

#----- content starts here -----
"""
Suppose there is a door whose height and width are unknown, and a pole whose length is also unknown.
When the pole is placed horizontally, it does not extend beyond 4 chi. When placed vertically, it does not extend beyond 2 chi. When placed diagonally, it fits perfectly.

Question: What are the width, height, and diagonal length of the door?

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from fractions import Fraction
import math

# Given dimensions
horizontal = 4  # chi
vertical = 2    # chi

# Calculate the diagonal length using the Pythagorean theorem
diagonal = math.sqrt(horizontal**2 + vertical**2)

# Convert diagonal length to zhang (1 zhang = 10 chi)
diagonal_in_zhang = Fraction(diagonal, 10)

# Assign results
a = horizontal  # width in chi
b = vertical    # height in chi
c = diagonal_in_zhang  # diagonal in zhang

# Results
a, b, c#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""

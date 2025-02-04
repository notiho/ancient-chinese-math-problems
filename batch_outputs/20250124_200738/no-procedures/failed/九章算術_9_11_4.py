"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

#----- content starts here -----
"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When the pole is placed horizontally, it cannot pass through the door by 4 chi.
When the pole is placed vertically, it cannot pass through the door by 2 chi.
When the pole is placed diagonally, it just fits.

Question: What are the width, height, and length of the pole?

Answer: The width is *a* chi, the height is *b* chi, and the length of the pole is *c* zhang.
"""

# Let the width of the door be `a` chi, the height of the door be `b` chi, and the length of the pole be `c` chi.

from fractions import Fraction

# Horizontal placement: the pole exceeds the width by 4 chi
# a = c - 4

# Vertical placement: the pole exceeds the height by 2 chi
# b = c - 2

# Diagonal placement: the pole just fits, so it satisfies the Pythagorean theorem
# c^2 = a^2 + b^2

# Substituting a = c - 4 and b = c - 2 into the Pythagorean theorem:
# c^2 = (c - 4)^2 + (c - 2)^2

# Expand the equation:
# c^2 = (c^2 - 8c + 16) + (c^2 - 4c + 4)
# c^2 = 2c^2 - 12c + 20

# Simplify:
# 0 = c^2 - 12c + 20

# Solve the quadratic equation for c:
# c = [12 ± sqrt(12^2 - 4(1)(20))] / 2(1)
# c = [12 ± sqrt(144 - 80)] / 2
# c = [12 ± sqrt(64)] / 2
# c = [12 ± 8] / 2

# Two solutions:
# c = (12 + 8) / 2 = 20 / 2 = 10
# c = (12 - 8) / 2 = 4 / 2 = 2

# Since the pole must be longer than both the width and height of the door, we take c = 10 chi.

# Calculate a and b:
c = 10  # Length of the pole in chi
a = c - 4  # Width of the door in chi
b = c - 2  # Height of the door in chi

# Convert c to zhang (1 zhang = 10 chi):
c_in_zhang = Fraction(c, 10)

# Final results:
a  # Width of the door in chi
b  # Height of the door in chi
c_in_zhang  # Length of the pole in zhang#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 10"""

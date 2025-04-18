"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

#----- content starts here -----
"""
Suppose there is a door whose height and width are unknown, and a pole whose length is also unknown.
When the pole is placed horizontally, it does not extend beyond 4 chi.
When the pole is placed vertically, it does not extend beyond 2 chi.
When the pole is placed diagonally, it fits exactly.

Question: What are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root. 
Divide the square root by 1. 
The result, when added to the vertical limit, gives the width of the door.
When added to the horizontal limit, it gives the height of the door.
Adding the two limits together gives the diagonal length of the door.

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from math import sqrt

# Horizontal limit (橫之不出)
橫 = 4  # chi

# Vertical limit (從之不出)
從 = 2  # chi

# Multiply horizontal and vertical limits, double the result, and take the square root
積 = 橫 * 從
倍積 = 2 * 積
開方 = sqrt(倍積)

# Calculate the width (戶廣)
戶廣 = 開方 + 從

# Calculate the height (戶高)
戶高 = 開方 + 橫

# Calculate the diagonal length (戶袤)
戶袤 = 橫 + 從

# Convert diagonal length to zhang (1 zhang = 10 chi)
戶袤_丈 = 戶袤 / 10

# Final results
a = 戶廣  # Width in chi
b = 戶高  # Height in chi
c = 戶袤_丈  # Diagonal length in zhang#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 0.6"""

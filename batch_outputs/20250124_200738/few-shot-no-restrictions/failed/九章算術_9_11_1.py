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
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root.
Divide by the result. Add the vertical limit to obtain the width of the door.
Add the horizontal limit to obtain the height of the door.
Add the two limits together to obtain the diagonal length of the door.

Answer: the width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from math import sqrt

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# Multiply the horizontal and vertical limits together, double the result, and take the square root
積 = 橫不出 * 從不出
倍積 = 2 * 積
開方 = sqrt(倍積)

# Add the vertical limit to obtain the width of the door
廣 = 開方 + 從不出

# Add the horizontal limit to obtain the height of the door
高 = 開方 + 橫不出

# Add the two limits together to obtain the diagonal length of the door
袤 = 橫不出 + 從不出

# Convert 袤 from chi to zhang (1 zhang = 10 chi)
袤 = 袤 / 10

a = 廣
b = 高
c = 袤#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 0.6"""

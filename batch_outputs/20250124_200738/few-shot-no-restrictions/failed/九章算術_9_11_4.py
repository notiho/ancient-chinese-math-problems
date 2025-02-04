"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

#----- content starts here -----
"""
Suppose there is a door whose height and width are unknown, and a pole whose length is unknown.
When the pole is placed horizontally, it does not extend beyond 4 chi.
When the pole is placed vertically, it does not extend beyond 2 chi.
When the pole is placed diagonally, it fits exactly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root. Divide by 1.
Add the vertical limit to the result to obtain the width of the door.
Add the horizontal limit to the result to obtain the height of the door.
Add the two limits together to obtain the diagonal length of the door.

Answer: the width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘
相乘 = 橫不出 * 從不出

# 倍
倍 = 2 * 相乘

# 開方
開方 = math.sqrt(倍)

# 戶廣
戶廣 = 開方 + 從不出

# 戶高
戶高 = 開方 + 橫不出

# 戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤丈 = 戶袤 / 10

# Final results
a = 戶廣  # 廣 in 尺
b = 戶高  # 高 in 尺
c = 戶袤丈  # 袤 in 丈#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 0.6"""

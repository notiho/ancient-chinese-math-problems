"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

#----- content starts here -----
"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When the pole is placed horizontally, it does not extend beyond 4 chi.
When the pole is placed vertically, it does not extend beyond 2 chi.
When the pole is placed diagonally, it fits exactly.

Question: What are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root. Divide by 1.
The result, when added to the vertical limit, gives the width of the door.
When added to the horizontal limit, it gives the height of the door.
Adding the two limits together gives the diagonal length of the door.

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from math import sqrt

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘，倍
積 = 橫不出 * 從不出 * 2

# 開方
對角線 = sqrt(積)

# 戶廣
戶廣 = 從不出 + 對角線

# 戶高
戶高 = 橫不出 + 對角線

# 戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤_丈 = 戶袤 / 10

# Final results
a = 戶廣
b = 戶高
c = 戶袤_丈#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 0.6"""

"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a(=6)尺 ，高 b(=8)尺 ，袤 c(=1)丈 。
"""

#----- content starts here -----
"""
Suppose there is a door, the height and width of which are unknown, and a pole, the length of which is also unknown.
When placed horizontally, it does not extend beyond 4 chi.
When placed vertically, it does not extend beyond 2 chi.
When placed diagonally, it fits exactly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the vertical and horizontal limits together, double the result, and take the square root. Divide by it.
Add the result to the vertical limit to get the width of the door.
Add the result to the horizontal limit to get the height of the door.
Add the two limits together to get the diagonal length of the door.

Answer: the width is *a*(=6) chi, the height is *b*(=8) chi, and the diagonal length is *c*(=1) zhang.
"""

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘
相乘 = 橫不出 * 從不出

# 倍
倍 = 2 * 相乘

# 而開方除之
開方 = math.sqrt(倍)

# 所得加從不出即戶廣
戶廣 = 開方 + 從不出

# 加橫不出即戶高
戶高 = 開方 + 橫不出

# 兩不出加之，得戶袤
戶袤 = 橫不出 + 從不出

# Convert results to appropriate units
a = int(戶廣)  # 6 尺
b = int(戶高)  # 8 尺
c = int(戶袤 / 10)  # 1 丈#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 0"""

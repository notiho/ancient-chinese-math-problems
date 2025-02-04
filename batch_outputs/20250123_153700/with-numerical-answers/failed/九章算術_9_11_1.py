"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a(=6)尺 ，高 b(=8)尺 ，袤 c(=1)丈 。
"""

"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When placed horizontally, the pole does not exceed 4 chi.
When placed vertically, the pole does not exceed 2 chi.
When placed diagonally, it just fits.

Question: What are the height, width, and diagonal length of the door?

The procedure says: Multiply the vertical and horizontal limits together, double the result, and take the square root of it.
Divide by this square root.
Add the vertical limit to the result to obtain the width of the door.
Add the horizontal limit to the result to obtain the height of the door.
Add the two limits together to obtain the diagonal length of the door.

Answer: The width is *a*(=6) chi, the height is *b*(=8) chi, and the diagonal length is *c*(=1) zhang.
"""

from fractions import Fraction

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘
積 = 橫不出 * 從不出

# 倍
積倍 = 2 * 積

# 開方 (manually calculating square root for simplicity)
開方 = Fraction(積倍).sqrt()

# 戶廣
a = 開方 + 從不出  # 6

# 戶高
b = 開方 + 橫不出  # 8

# 戶袤
c = 橫不出 + 從不出  # 1丈 (10尺)
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

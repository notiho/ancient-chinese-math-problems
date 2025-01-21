"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a(=6)尺 ，高 b(=8)尺 ，袤 c(=1)丈 。
"""

"""
Suppose there is a door of unknown height and width, and a rod of unknown length.
When placed horizontally, the rod does not extend beyond 4 chi.
When placed vertically, the rod does not extend beyond 2 chi.
When placed diagonally, the rod fits exactly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root.
Divide by this square root. Add the result to the vertical limit to obtain the width of the door.
Add the result to the horizontal limit to obtain the height of the door.
Add the two limits together to obtain the diagonal length of the door.

Answer: the width is *a*(=6) chi, the height is *b*(=8) chi, and the diagonal length is *c*(=1) zhang.
"""

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘
積 = 橫不出 * 從不出

# 倍
倍積 = 2 * 積

# 開方
開方 = math.sqrt(倍積)

# 戶廣
a = 橫不出 + 開方  # 6 尺

# 戶高
b = 從不出 + 開方  # 8 尺

# 戶袤
c = 橫不出 + 從不出  # 1 丈
"""
Variable 'a' has wrong value. Expected: 6, Actual: 8.0
Variable 'b' has wrong value. Expected: 8, Actual: 6.0
Variable 'c' has wrong value. Expected: 1, Actual: 6"""

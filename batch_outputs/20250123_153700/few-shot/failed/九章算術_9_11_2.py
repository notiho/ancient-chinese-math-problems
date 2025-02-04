"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When placed horizontally, the pole does not extend beyond 4 chi.
When placed vertically, the pole does not extend beyond 2 chi.
When placed diagonally, the pole fits exactly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and then take the square root.
The result, when added to the vertical limit, gives the width of the door.
When added to the horizontal limit, it gives the height of the door.
Adding the two limits together gives the diagonal length of the door.

Answer: the width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘
積 = 橫不出 * 從不出

# 倍
倍積 = 2 * 積

# 開方除之 (taking the square root)
平方根 = Fraction(倍積).sqrt()

# 所得加從不出即戶廣
戶廣 = 平方根 + 從不出

# 所得加橫不出即戶高
戶高 = 平方根 + 橫不出

# 兩不出加之，得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤丈 = Fraction(戶袤, 10)

a = 戶廣
b = 戶高
c = 戶袤丈
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

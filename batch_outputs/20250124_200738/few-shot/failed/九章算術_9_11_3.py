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

The procedure says: Multiply the horizontal and vertical limits together, double the result, and then take the square root.
Divide by this result.
Add the vertical limit to obtain the width of the door.
Add the horizontal limit to obtain the height of the door.
Add the two limits together to obtain the diagonal length of the door.

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

# 開方
平方根 = Fraction(倍積).sqrt()

# 戶廣
戶廣 = 平方根 + 從不出

# 戶高
戶高 = 平方根 + 橫不出

# 戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤丈 = Fraction(戶袤, 10)

a = 戶廣
b = 戶高
c = 戶袤丈#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a(=6)尺 ，高 b(=8)尺 ，袤 c(=1)丈 。
"""

#----- content starts here -----
"""
Suppose there is a door whose height and width are unknown, and a pole whose length is also unknown.
When the pole is placed horizontally, it does not extend beyond 4 chi.
When placed vertically, it does not extend beyond 2 chi.
When placed diagonally, it fits exactly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root.
Divide by this result.
Add the vertical limit to the result to obtain the door's width.
Add the horizontal limit to the result to obtain the door's height.
Add the two limits together to obtain the diagonal length.

Answer: The width is *a*(=6) chi, the height is *b*(=8) chi, and the diagonal length is *c*(=1) zhang.
"""

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘，倍
積 = 2 * (橫不出 * 從不出)

# 而開方除之 (開方即平方根)
平方根 = Fraction(積).sqrt()

# 所得加從不出即戶廣
a = 平方根 + 從不出  # 廣 = 6 尺

# 所得加橫不出即戶高
b = 平方根 + 橫不出  # 高 = 8 尺

# 兩不出加之，得戶袤
c = 橫不出 + 從不出  # 袤 = 1 丈 (10 尺)#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

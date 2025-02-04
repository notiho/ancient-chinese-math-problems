"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a(=6)尺 ，高 b(=8)尺 ，袤 c(=1)丈 。
"""

#----- content starts here -----
"""
Suppose there is a door with unknown height and width, and a pole with unknown length.
When placed horizontally, it does not extend beyond 4 chi.
When placed vertically, it does not extend beyond 2 chi.
When placed diagonally, it fits perfectly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root of it.
Divide by the diagonal to find the width of the door by adding the vertical limit, and the height of the door by adding the horizontal limit.
Add the two limits together to find the diagonal length of the door.

Answer: the width is *a*(=6) chi, the height is *b*(=8) chi, and the diagonal is *c*(=1) zhang.
"""

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 邪之適出
邪適出 = (橫不出**2 + 從不出**2)**0.5

# 戶廣
a = 橫不出

# 戶高
b = round(邪適出)

# 戶袤
c = round(10#----- content ends here -----

"""
Code error: '(' was never closed (<string>, line 32)"""

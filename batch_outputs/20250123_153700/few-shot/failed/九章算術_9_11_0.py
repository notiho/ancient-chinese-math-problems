"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
Suppose there is a door whose height and width are unknown, and a pole whose length is also unknown.
When placed horizontally, the pole does not extend beyond 4 chi.
When placed vertically, the pole does not extend beyond 2 chi.
When placed diagonally, it fits exactly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits together, double the result, and take the square root.
Divide by this result. Add the vertical limit to obtain the width of the door.
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

# 開方 (square root)
# Since we cannot use external libraries, we use an iterative method to approximate the square root.
def 開方(x):
    guess = x / 2
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

開方積 = 開方(倍積)

# 所得加從不出即戶廣
戶廣 = 開方積 + 從不出

# 所得加橫不出即戶高
戶高 = 開方積 + 橫不出

# 兩不出加之，得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤丈 = 戶袤 / 10

a = 戶廣
b = 戶高
c = 戶袤丈
"""
Variable 'c' has wrong value. Expected: 1, Actual: 0.6"""

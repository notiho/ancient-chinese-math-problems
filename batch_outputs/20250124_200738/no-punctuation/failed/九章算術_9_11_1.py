"""
今有戶不知高廣竿不知長短橫之不出四尺從之不出二尺邪之適出問戶高廣袤各幾何
術曰從橫不出相乘倍而開方除之所得加從不出即戶廣加橫不出即戶高兩不出加之得戶袤
荅曰廣 a尺 高 b尺 袤 c丈 
"""

#----- content starts here -----
"""
Suppose there is a door, but its height and width are unknown. There is a pole of unknown length.
When placed horizontally, it does not extend beyond the door by 4 chi.
When placed vertically, it does not extend beyond the door by 2 chi.
When placed diagonally, it just fits perfectly.
Question: what are the width, height, and diagonal length of the door?

The procedure says: Multiply the horizontal "does not extend" and the vertical "does not extend" together, double it, and take the square root. Divide by the diagonal "does not extend."
Add the vertical "does not extend" to the result to obtain the width of the door.
Add the horizontal "does not extend" to the result to obtain the height of the door.
Add the horizontal and vertical "does not extend" together to obtain the diagonal length of the door.

Answer: the width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 邪之適出
邪適出 = 1  # In terms of diagonal, this is the unit.

# 橫不出相乘倍而開方除之所得
積 = 橫不出 * 從不出
倍積 = 2 * 積
平方根 = (倍積) ** 0.5
所得 = 平方根 / 邪適出

# 加從不出即戶廣
戶廣 = 所得 + 從不出

# 加橫不出即戶高
戶高 = 所得 + 橫不出

# 兩不出加之得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (10 尺 = 1 丈)
戶袤丈 = 戶袤 / 10

a = 戶廣
b = 戶高
c = 戶袤丈#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 0.6"""

"""
今有戶不知高廣竿不知長短橫之不出四尺從之不出二尺邪之適出問戶高廣袤各幾何
術曰從橫不出相乘倍而開方除之所得加從不出即戶廣加橫不出即戶高兩不出加之得戶袤
荅曰廣 a尺 高 b尺 袤 c丈 
"""

"""
Suppose there is a door, but its height and width are unknown. There is a pole, but its length is also unknown.
When the pole is placed horizontally, it does not extend beyond the door by 4 chi.
When the pole is placed vertically, it does not extend beyond the door by 2 chi.
When the pole is placed diagonally, it just fits the door.
Question: what are the width, height, and diagonal length of the door?

The procedure says: Multiply the horizontal "does not extend" and the vertical "does not extend" together, double the result, and take the square root. Divide by 1, and the result obtained is added to the vertical "does not extend" to get the door's width. Add the horizontal "does not extend" to get the door's height. Add the two "does not extend" values together to get the diagonal length of the door.

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 橫不出相乘倍
積 = 橫不出 * 從不出 * 2

# 開方除之所得
平方根 = math.sqrt(積)

# 加從不出即戶廣
戶廣 = 平方根 + 從不出

# 加橫不出即戶高
戶高 = 平方根 + 橫不出

# 兩不出加之得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤丈 = Fraction(戶袤, 10)

a = Fraction(戶廣)
b = Fraction(戶高)
c = 戶袤丈
"""
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""

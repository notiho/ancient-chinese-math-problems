"""
今有戶不知高廣竿不知長短橫之不出四尺從之不出二尺邪之適出問戶高廣袤各幾何
術曰從橫不出相乘倍而開方除之所得加從不出即戶廣加橫不出即戶高兩不出加之得戶袤
荅曰廣 a尺 高 b尺 袤 c丈 
"""

"""
Suppose there is a door, but its height and width are unknown. There is a pole, but its length is also unknown.
When placed horizontally, it does not extend beyond 4 chi (horizontal limit).
When placed vertically, it does not extend beyond 2 chi (vertical limit).
When placed diagonally, it just fits perfectly.
Question: what are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal limit and the vertical limit together, double the result, and take the square root.
Divide by 2, and the result obtained is added to the vertical limit to get the width of the door.
Add the horizontal limit to get the height of the door.
Add the two limits together to get the diagonal length of the door.

Answer: the width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 橫不出相乘倍而開方
積 = 橫不出 * 從不出 * 2
平方根 = math.sqrt(積)

# 除之所得
所得 = Fraction(平方根, 2)

# 加從不出即戶廣
廣 = 所得 + 從不出

# 加橫不出即戶高
高 = 所得 + 橫不出

# 兩不出加之得戶袤
袤 = 橫不出 + 從不出

# Convert 袤 to 丈 (1 丈 = 10 尺)
袤 = Fraction(袤, 10)

a = 廣
b = 高
c = 袤
"""
Code error: both arguments should be Rational instances"""

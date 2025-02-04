"""
今有戶不知高廣竿不知長短橫之不出四尺從之不出二尺邪之適出問戶高廣袤各幾何
術曰從橫不出相乘倍而開方除之所得加從不出即戶廣加橫不出即戶高兩不出加之得戶袤
荅曰廣 a尺 高 b尺 袤 c丈 
"""

"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When placed horizontally, it does not extend beyond 4 chi.
When placed vertically, it does not extend beyond 2 chi.
When placed diagonally, it just fits.
Question: What are the height, width, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical limits (4 and 2) together, double the result, and take the square root.
Divide this by 2, and the result added to the vertical limit gives the width of the door.
The result added to the horizontal limit gives the height of the door.
Adding both limits together gives the diagonal length of the door.

Answer: The width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 橫不出相乘
相乘 = 橫不出 * 從不出

# 倍而開方
倍開方 = math.sqrt(2 * 相乘)

# 除之所得
所得 = Fraction(倍開方, 2)

# 加從不出即戶廣
戶廣 = 所得 + 從不出

# 加橫不出即戶高
戶高 = 所得 + 橫不出

# 兩不出加之得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 from chi to zhang (1 zhang = 10 chi)
戶袤_丈 = Fraction(戶袤, 10)

a = 戶廣
b = 戶高
c = 戶袤_丈
"""
Code error: both arguments should be Rational instances"""
